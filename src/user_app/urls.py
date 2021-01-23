from django import forms
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import PasswordResetCheckedEmailForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_app/logout.html'), name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='user_app/password_reset.html', form_class=PasswordResetCheckedEmailForm), name='password_reset'),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='user_app/password_reset_done.html'), name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='user_app/password_reset_confirm.html'), name='password_reset_confirm'),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='user_app/password_reset_complete.html'), name='password_reset_complete'),

    path('register/', views.register, name='register'),
    path('profile/', views.display_profile_page, name='profile'),
]
