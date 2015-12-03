from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from cuentas.forms import RegisterForm
from django.views.generic import TemplateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.auth.models import User


class LoginDir(SuccessMessageMixin, FormView):
    form_class = AuthenticationForm
    template_name = "home.html"
    success_url = reverse_lazy("cuenta:sesion")
    success_message = "Welcome back %(username)s!"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            print(True)
            return redirect(self.get_success_url())
        else:
            print(False)
            return super(LoginDir, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginDir, self).form_valid(form)


class Registro(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = "registro.html"
    success_url = reverse_lazy("cuenta:home")
    success_message = "User was created successfully"


class Cambio(UpdateView):
    """docstring for Cambio"""
    form_class=RegisterForm
    template_name= "registro.html"
    success_url = reverse_lazy("cuenta:home")


class Sesion(ListView):
    model = User
    template_name = "mainalt.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Sesion, self).dispatch(self.request, *args, **kwargs)


class Logout(RedirectView):
    pattern_name = 'cuenta:home'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).get(request, *args, **kwargs)
