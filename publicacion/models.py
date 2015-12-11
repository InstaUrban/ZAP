from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Publica(models.Model):
    """docstring for tip_not"""
    id_user = models.ForeignKey(User)
    publicacion = models.TextField(max_length=300, blank=False)
    image = models.ImageField(upload_to="img/img_usr", null=True, blank=True)
    like = models.IntegerField(null=True, blank=True,default=0)
    dislike = models.IntegerField(null=True, blank=True,default=0)

    def get_image(self):
        try:
            return '<img src="%s" style="display: block; width: 60px;"/>' % self.image.url
        except:
            return "<h3>No image</h3>"
    get_image.allow_tags = True
