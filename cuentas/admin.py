from django.contrib import admin
from cuentas.models import Usuarios, Tipnot, Noticia
admin.site.register([Usuarios, Tipnot, Noticia])
# Register your models here.
