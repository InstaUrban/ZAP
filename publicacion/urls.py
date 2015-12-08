from django.conf.urls import url
from publicacion.views import Publicaon, Publicadet

urlpatterns = [
    url(r'^publicacion/', Publicaon.as_view(), name="publicacion"),
    url(r'^publicaciondet/', Publicadet.as_view(), name="publicaciondet"),
]
