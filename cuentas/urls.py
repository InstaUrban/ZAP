"""ZAP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from cuentas.views import LoginDir, Registro, Logout, Sesion, Cambio

urlpatterns = [
    url(r'^home/$', LoginDir.as_view(), name="home"),
    url(r'^Registro/', Registro.as_view(), name="Registro"),
    url(r'^Cambio/(?P<pk>\d+)$', Cambio.as_view(), name='update'),
    url(r'^Logout/$', Logout.as_view(), name="Logout"),
    url(r'^sesion/$', Sesion.as_view(), name="sesion")
]
