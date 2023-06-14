from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from authent.forms.changepassword_form import PasswordChangeForm
from authent.forms.signup_form import SignUpForm
from authent.models.users import CustomUser


class HomeView(TemplateView):
    template_name = "common/home.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "common/dashboard.html"
    login_url = reverse_lazy("home")


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("dashboard")
    template_name = "common/register.html"
    model = CustomUser

    def post(self, request, *args, **kwargs):
        user = CustomUser.objects.create(
            email=request.POST["email"],
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
        )
        user.set_password(request.POST["password"])
        user.save()

        return super().post(request, *args, **kwargs)


class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("dashboard")
    template_name = "common/change-password.html"


# class LoginView():
#     form_class = LoginForm
#     template_name = 'common/login.html'
# pbkdf2_sha256$600000$q70peUwjkNDlQZNNwDQJEY$xl3W0anrqUwE8kO72vJNRfMYnAiq4eJzICCMLX2n/v8=
