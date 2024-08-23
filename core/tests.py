from django.test import TestCase
from django.urls import reverse
from .models import CustomUser  # Importando o modelo CustomUser

class AdminLoginTest(TestCase):

    def setUp(self):
        # Criar um usuário admin para teste
        self.admin_user = CustomUser.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpassword'
        )

    def test_login_required(self):
        # Tenta acessar a página de admin sem estar logado
        response = self.client.get(reverse('admin:index'))
        self.assertRedirects(response, '/admin/login/?next=/admin/')

    def test_admin_login(self):
        # Faz login com o usuário admin
        self.client.login(username='admin', password='adminpassword')

        # Tenta acessar a página de admin
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'Administração do Django')
        self.assertContains(response, 'Django administration')              

    def test_admin_invalid_login(self):
        # Tenta fazer login com credenciais inválidas
        self.client.login(username='admin', password='wrongpassword')

        # Tenta acessar a página de admin
        response = self.client.get(reverse('admin:index'))
        self.assertRedirects(response, '/admin/login/?next=/admin/')
