from rest_framework import serializers
from .models import *

class EnfermedadesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enfermedades
        fields = (
        'id', 'nombre', 'descripcion', 'calificacion', 'tag', 'email', 'telefono',
         'comentario',)
