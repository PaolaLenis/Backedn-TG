from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
from categorias.models import Categoria
from comentarios.models import Comentario
from tags.models import Tag
from usuarios.models import Usuario

from rest_framework.reverse import reverse as api_reverse


class Enfermedades(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=400)
    calificacion = models.DecimalField(max_digits=30, decimal_places=25)
    tag = models.ManyToManyField(Tag)
    email = ArrayField(models.CharField(max_length=100, blank=True))
    comentario = models.ManyToManyField(Comentario, blank=True)

    def get_api_url(self, request=None):
        return api_reverse("", kwargs={'id': self.id}, request=request)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

class RecomendacionRutinas(models.Model):
    id = models.AutoField(primary_key=True)
    valor = models.CharField(max_length=100)
    enfermedad = models.ForeignKey(Enfermedades, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.valor

    def __str__(self):
        return self.valor
