from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import models, middlewares, forms


class RegistrationView(CreateView):
    form_class = forms.CustomRegistrationForm
    template_name = "users/register.html"
    success_url = "/login/"

    def form_valid(self, form):
        response = super().form_valid(form)
        exp = form.cleaned_data["experience"]
        if exp < 1:
            self.object.club = "Новичок"
        elif 1 <= exp <= 2:
            self.object.club = "не Новичок"
        elif 2 <= exp <= 3:
            self.object.club = "Старейшина"
        elif 3 <= exp <= 5:
            self.object.club = "Профи"
        elif exp > 5:
            self.object.club = "Книжный гуру"
        else:
            self.object.club = "Без опыта"

        self.object.save()
        return response


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "users/login.html"

    def get_success_url(self):
        return reverse("users:user_list")


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy("user:login")


class UserListView(ListView):
    template_name = "users/user_list.html"
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["club"] = getattr(self.request, "club", "Без опыта")
        return context
