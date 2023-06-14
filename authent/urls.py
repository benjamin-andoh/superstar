from authent.views.authenticate import ChangePasswordView, DashboardView, HomeView,  SignUpView
from django.contrib.auth import views as auth_views
from django.urls import path
# app_name = 'authent'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("register/", SignUpView.as_view(), name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="common/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("change-password", ChangePasswordView.as_view(), name="change-password"),
    # Forget Password
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="common/password-reset/password_reset.html",
            subject_template_name="common/password-reset/password_reset_subject.txt",
            email_template_name="common/password-reset/password_reset_email.html",
            success_url="done",
        ),
        name="password-reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="common/password-reset/password_reset_done.html"
        ),
        name="done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="common/password-reset/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="common/password-reset/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
