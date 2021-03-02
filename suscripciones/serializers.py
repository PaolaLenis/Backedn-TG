from rest_framework import serializers
from .models import *


class SuscripcionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Suscripcion
        fields = ('id', 'usuario', 'lugar', 'fecha_suscripcion', 'hora_suscripcion', 'notificaciones')
        #depth = 1

