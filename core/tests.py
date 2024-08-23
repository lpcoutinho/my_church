from django.test import TestCase
from django.urls import reverse

from .models import Congregation, CustomUser


class AdminLoginTest(TestCase):
    def setUp(self):
        # Criar um usuário admin para teste
        self.admin_user = CustomUser.objects.create_superuser(
            username="admin", email="admin@example.com", password="adminpassword"
        )

    def test_login_required(self):
        # Tenta acessar a página de admin sem estar logado
        response = self.client.get(reverse("admin:index"))
        self.assertRedirects(response, "/admin/login/?next=/admin/")

    def test_admin_login(self):
        # Faz login com o usuário admin
        self.client.login(username="admin", password="adminpassword")

        # Tenta acessar a página de admin
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'Administração do Django')
        self.assertContains(response, "Django administration")

    def test_admin_invalid_login(self):
        # Tenta fazer login com credenciais inválidas
        self.client.login(username="admin", password="wrongpassword")

        # Tenta acessar a página de admin
        response = self.client.get(reverse("admin:index"))
        self.assertRedirects(response, "/admin/login/?next=/admin/")


class HomePageTests(TestCase):
    def setUp(self):
        # Criar um objeto Congregation para ser usado no teste
        self.congregation = Congregation.objects.create(
            name="My Church", address="Rua dos Bobos, 0"
        )

    def test_home_page_status_code(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_header_and_footer(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<header>")
        self.assertContains(response, "</header>")
        self.assertContains(response, "<footer>")
        self.assertContains(response, "</footer>")

    def test_home_page_displays_congregation_info(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, self.congregation.name)
        self.assertContains(response, self.congregation.address)


class ContactPageTests(TestCase):
    def test_contact_page_status_code(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_contains_correct_content(self):
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "<h2>Contact Me</h2>")
        self.assertContains(response, "coutinholps@gmail.com")
        self.assertContains(response, "https://wa.me/5521964781930")
        self.assertContains(response, "https://www.linkedin.com/in/luizpaulocoutinho/")

    def test_contact_page_contains_clickable_email(self):
        response = self.client.get(reverse("contact"))
        self.assertContains(
            response, '<a href="mailto:coutinholps@gmail.com">coutinholps@gmail.com</a>'
        )

    def test_contact_page_contains_clickable_phone(self):
        response = self.client.get(reverse("contact"))
        self.assertContains(
            response, '<a href="https://wa.me/5521964781930">+55 21 964 781 930</a>'
        )

    def test_contact_page_contains_clickable_linkedin(self):
        response = self.client.get(reverse("contact"))
        self.assertContains(
            response,
            '<a href="https://www.linkedin.com/in/luizpaulocoutinho/" target="_blank" '
            'rel="noopener noreferrer">Luiz Paulo Coutinho</a>',
        )

    def test_contact_page_uses_base_template(self):
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "base.html")
