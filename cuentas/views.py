from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from cuentas.forms import RegisterForm, UpdateForm, UpdateImg, UpdateAmg
from django.views.generic import TemplateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.auth.models import User
from cuentas.models import Usuarios, Amigo


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
    model = User
    form_class = UpdateForm
    template_name = "cambio.html"
    success_url = reverse_lazy("cuenta:sesion")


class Friend(CreateView):
    """docstring for Cambio"""
    model = Amigo
    template_name = "Amigo.html"
    success_url = reverse_lazy("cuenta:sesion")
    form_class = UpdateAmg


class CambioPerfil(UpdateView):
    """docstring for Cambio"""
    model = Usuarios
    #    form_class = UpdateImg
    fields = ['image']
    template_name = "cambioimg.html"
    success_url = reverse_lazy("cuenta:sesion")


class Sesion(ListView):
    model = Usuarios
    template_name = "mainalt.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        self.queryset = Usuarios.objects.filter(id_persona=user.id)
        return super(Sesion, self).dispatch(self.request, *args, **kwargs)


class VerAmg(ListView):
    model = Usuarios
    template_name = "amigosd.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.queryset = Usuarios.objects.all()
        return super(VerAmg, self).dispatch(self.request, *args, **kwargs)


class Logout(RedirectView):
    pattern_name = 'cuenta:home'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).get(request, *args, **kwargs)
