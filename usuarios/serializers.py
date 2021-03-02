from rest_framework import serializers
from .models import *


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'uid', 'nombre', 'email',  'telefono', 'genero')
