from django.forms import ModelForm
from django.contrib.auth.models import User
from publicacion.models import Publica

# Create the form class.


class Publicaform(ModelForm):

    class Meta:
        model = Publica
        fields = ['publicacion', 'image']

    def save(self, commit=True):
        publica = super(Publicaform, self).save(commit=False)
        publica.id_user = User
        if commit:
            publica.save()
        return publica
