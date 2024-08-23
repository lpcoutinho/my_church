from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("contact/", views.contact_page, name="contact"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("signup/", views.signup_page, name="signup"),
    path("donation/", views.donation_page, name="donation"),
    path(
        "donation/confirmation/<int:donation_id>/",
        views.donation_confirmation,
        name="donation_confirmation",
    ),
]
