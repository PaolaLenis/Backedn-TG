from django.contrib.postgres.fields import ArrayField
from django.db import models
from rest_framework.reverse import reverse as api_reverse

# Create your models here.
from usuarios.models import Usuario


class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_lugar = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15, blank=True)
    email = ArrayField(models.CharField(max_length=50, blank=True))
    informacion = models.CharField(max_length=200)
    aceptado = models.BooleanField(default=False)

    def get_api_url(self, request=None):
        return api_reverse("api-request:request-rud", kwargs={'id': self.id}, request=request)

    def __unicode__(self):
        return self.informacion

    def __str__(self):
        return self.informacion
