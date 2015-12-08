from django.forms import ModelForm
from django.contrib.auth.models import User
from cuentas.models import Usuarios, Amigo
from django import forms

# Create the form class.


class RegisterForm(ModelForm):
    error_messages = {
        'password_mismatch': ("las contraseñas no coinciden"),
    }
    password1 = forms.CharField(label=(
        "Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=(
        "Password confirmation"),
        widget=forms.PasswordInput,
        help_text=("Enter the same password as above, for verification."))
    telephone = forms.CharField(label=("telephone"))
    date = forms.DateField(label=("birthday"))

    class Meta:
        model = User
        fields = ("username", 'first_name', 'last_name', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        Usuarios.objects.create(id_persona=user, tel=self.cleaned_data[
            "telephone"], fecha=self.cleaned_data["date"])
        Amigo.objects.create(usr1=user)
        return user


class UpdateForm(ModelForm):
    error_messages = {
        'password_mismatch': ("las contraseñas no coinciden"),
    }
    password1 = forms.CharField(label=(
        "Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=(
        "Password confirmation"),
        widget=forms.PasswordInput,
        help_text=("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username", 'first_name', 'last_name', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UpdateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UpdateImg(ModelForm):

    class Meta:
        model = Usuarios
        fields = ['image']

    def save(self, commit=True):
        usuarios = super(UpdateImg, self).save(commit=False)
        usuarios.id_persona = User
        if commit:
            usuarios.save()
        return usuarios


class UpdateAmg(ModelForm):

    class Meta:
        model = Amigo
        fields = ['usr2']

    def save(self, commit=True):
        amigo = super(UpdateAmg, self).save(commit=False)
        amigo.usr1 = User
        if commit:
            amigo.usr1.usr2.add(amigo)
        return amigo
