from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Congregation, CustomUser, Donation

# Obtém o modelo de usuário configurado
User = get_user_model()


class AdminLoginTest(TestCase):
    """Testes para a funcionalidade de login do administrador."""

    def setUp(self):
        """Configuração inicial para criar um usuário admin para teste."""
        self.admin_user = CustomUser.objects.create_superuser(
            username="admin", email="admin@example.com", password="adminpassword"
        )

    def test_login_required(self):
        """Verifica se a página de admin exige autenticação."""
        response = self.client.get(reverse("admin:index"))
        self.assertRedirects(response, "/admin/login/?next=/admin/")

    def test_admin_login(self):
        """Verifica se o admin consegue fazer login com credenciais válidas."""
        self.client.login(username="admin", password="adminpassword")
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django administration")

    def test_admin_invalid_login(self):
        """Verifica se o login com credenciais inválidas falha corretamente."""
        self.client.login(username="admin", password="wrongpassword")
        response = self.client.get(reverse("admin:index"))
        self.assertRedirects(response, "/admin/login/?next=/admin/")


class HomePageTests(TestCase):
    """Testes para a página inicial."""

    def setUp(self):
        """Configuração inicial para criar uma congregação para teste."""
        self.congregation = Congregation.objects.create(
            name="My Church", address="Rua dos Bobos, 0"
        )

    def test_home_page_status_code(self):
        """Verifica se a página inicial retorna status 200."""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_header_and_footer(self):
        """Verifica se a página inicial contém header e footer."""
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<header>")
        self.assertContains(response, "</header>")
        self.assertContains(response, "<footer>")
        self.assertContains(response, "</footer>")

    def test_home_page_displays_congregation_info(self):
        """Verifica se as informações da congregação são exibidas na página inicial."""
        response = self.client.get(reverse("home"))
        self.assertContains(response, self.congregation.name)
        self.assertContains(response, self.congregation.address)


class ContactPageTests(TestCase):
    """Testes para a página de contato."""

    def test_contact_page_status_code(self):
        """Verifica se a página de contato retorna status 200."""
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_contains_correct_content(self):
        """Verifica se a página de contato contém o conteúdo correto."""
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "<h2>Contact Me</h2>")
        self.assertContains(response, "coutinholps@gmail.com")
        self.assertContains(response, "https://wa.me/5521964781930")
        self.assertContains(response, "https://www.linkedin.com/in/luizpaulocoutinho/")

    def test_contact_page_contains_clickable_email(self):
        """Verifica se o e-mail na página de contato é clicável."""
        response = self.client.get(reverse("contact"))
        self.assertContains(
            response, '<a href="mailto:coutinholps@gmail.com">coutinholps@gmail.com</a>'
        )

    def test_contact_page_contains_clickable_phone(self):
        """Verifica se o número de telefone na página de contato é clicável."""
        response = self.client.get(reverse("contact"))
        self.assertContains(
            response, '<a href="https://wa.me/5521964781930">+55 21 964 781 930</a>'
        )

    def test_contact_page_contains_clickable_linkedin(self):
        """Verifica se o link do LinkedIn na página de contato é clicável."""
        response = self.client.get(reverse("contact"))
        self.assertContains(
            response,
            '<a href="https://www.linkedin.com/in/luizpaulocoutinho/" target="_blank" '
            'rel="noopener noreferrer">Luiz Paulo Coutinho</a>',
        )

    def test_contact_page_uses_base_template(self):
        """Verifica se a página de contato utiliza o template base."""
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "base.html")


class UserAuthenticationTests(TestCase):
    """Testes para a autenticação de usuários."""

    def setUp(self):
        """Configuração inicial para criar um usuário para teste."""
        self.login_url = reverse("login")
        self.signup_url = reverse("signup")
        self.home_url = reverse("home")
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "securepassword123",
        }
        CustomUser.objects.create_user(**self.user_data)

    def test_login_page_status_code(self):
        """Verifica se a página de login retorna status 200."""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)

    def test_signup_page_status_code(self):
        """Verifica se a página de signup retorna status 200."""
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)

    def test_login_with_valid_credentials(self):
        """Verifica se o login com credenciais válidas redireciona corretamente."""
        response = self.client.post(
            self.login_url,
            {
                "username": self.user_data["username"],
                "password": self.user_data["password"],
            },
        )
        self.assertRedirects(response, self.home_url)

    def test_login_with_invalid_credentials(self):
        """Verifica se o login com credenciais inválidas retorna a mensagem correta."""
        response = self.client.post(
            self.login_url,
            {"username": self.user_data["username"], "password": "wrongpassword"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a correct username and password")

    def test_signup_with_valid_data(self):
        """Verifica se o signup com dados válidos redireciona corretamente."""
        response = self.client.post(
            self.signup_url,
            {
                "username": "newuser",
                "email": "newuser@example.com",
                "password1": "newsecurepassword123",
                "password2": "newsecurepassword123",
            },
        )
        self.assertRedirects(response, self.home_url)
        self.assertTrue(CustomUser.objects.filter(username="newuser").exists())

    def test_signup_with_invalid_data(self):
        """
        Verifica se o signup com dados inválidos retorna as mensagens de erro corretas.
        """
        response = self.client.post(
            self.signup_url,
            {
                "username": "",
                "email": "invalidemail",
                "password1": "pass",
                "password2": "word",
            },
        )
        # print(response.content.decode())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")
        self.assertContains(response, "Enter a valid email address.")
        self.assertContains(
            response, "Your password must contain at least 8 characters."
        )
        self.assertContains(response, "The two password fields didn’t match.")

    def test_logout(self):
        """Verifica se o logout redireciona para a página inicial."""
        self.client.login(
            username=self.user_data["username"], password=self.user_data["password"]
        )
        response = self.client.get(reverse("logout"))
        self.assertRedirects(response, self.home_url)


class DonationPageTests(TestCase):
    """Testes para a página de doações."""

    def setUp(self):
        """Configuração inicial para criar um usuário e definir a URL de doação."""
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="password"
        )
        self.donation_url = reverse("donation")

    def test_donation_page_status_code(self):
        """Verifica se a página de doação retorna status 200."""
        response = self.client.get(self.donation_url)
        self.assertEqual(response.status_code, 200)

    def test_donation_form_display(self):
        """Verifica se o formulário de doação é exibido corretamente."""
        response = self.client.get(self.donation_url)
        self.assertContains(response, "Make a Donation")
        self.assertContains(
            response, '<input type="text" id="amount" name="amount_display" required>'
        )

    @patch("core.views.PaymentProcessor.create_payment")
    def test_donation_process_and_redirect(self, mock_create_payment):
        """Testa o processo de doação e redirecionamento com um pagamento simulado."""
        mock_create_payment.return_value = {
            "date_created": "2024-08-23T00:00:00Z",
            "id": "123456789",
            "last_updated": "2024-08-23T00:00:00Z",
            "qr_code": "sample_qr_code",
            "qr_code_base64": "sample_qr_code_base64",
            "ticket_url": "https://sample.ticket.url",
        }

        response = self.client.post(
            self.donation_url,
            {"donation_type": "DO", "payment_method": "PIX", "amount": "10.00"},
        )

        donation = Donation.objects.last()
        self.assertRedirects(
            response, reverse("donation_confirmation", args=[donation.id])
        )
        self.assertEqual(donation.payment_status, "pending")
        self.assertEqual(donation.payment_id, "123456789")
        self.assertEqual(donation.qr_code, "sample_qr_code")
        self.assertEqual(donation.qr_code_base64, "sample_qr_code_base64")
        self.assertEqual(donation.ticket_url, "https://sample.ticket.url")

    def test_donation_confirmation_page(self):
        """
        Verifica se a página de confirmação de doação exibe o QR code e o código Pix.
        """
        donation = Donation.objects.create(
            donation_type="DO",
            payment_method="PIX",
            amount="10.00",
            qr_code="sample_qr_code",
            qr_code_base64="sample_qr_code_base64",
            ticket_url="https://sample.ticket.url",
        )

        response = self.client.get(reverse("donation_confirmation", args=[donation.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, "sample_qr_code_base64"
        )  # Verifica a imagem do QR code
        self.assertContains(response, "sample_qr_code")  # Verifica o código Pix
        self.assertContains(
            response, "<textarea", html=False
        )  # Verifica se o campo textarea está presente
        self.assertContains(
            response, "readonly", html=False
        )  # Verifica se o atributo readonly está presente


class DonationFormFrontendTests(TestCase):
    """Testes para o frontend do formulário de doação."""

    def test_amount_field_formatting(self):
        """Verifica se o campo Amount é formatado corretamente no frontend."""
        response = self.client.get(reverse("donation"))
        self.assertContains(
            response, '<input type="text" id="amount" name="amount_display" required>'
        )

        self.client.post(
            reverse("donation"),
            {
                "donation_type": "DO",
                "payment_method": "PIX",
                "amount_display": "100",  # Simula a entrada 100, que deve ser 1.00
                "amount": "1.00",  # Valor convertido enviado
            },
        )
        donation = Donation.objects.last()
        self.assertEqual(donation.amount, 1.00)
