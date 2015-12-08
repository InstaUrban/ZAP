from publicacion.forms import Publicaform
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.auth.models import User
from publicacion.models import Publica


class Publicaon(CreateView):
    """docstring for Cambio"""
    model = Publica
    template_name = "publicacion.html"
    success_url = reverse_lazy("cuenta:sesion")
    fields = ['publicacion', 'image']

    def form_valid(self, form):
        user = self.request.user
        form.instance.id_user = user
        return super(Publicaon, self).form_valid(form)


class Publicadet(ListView):
    """docstring for Cambio"""
    model = Publica
    template_name = "publicaciond.html"

    def dispatch(self, request, *args, **kwargs):
        self.queryset = Publica.objects.all()
        return super(Publicadet, self).dispatch(self.request, *args, **kwargs)
