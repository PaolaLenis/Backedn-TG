from django.contrib import admin
# Register your models here.
from lugares.models import Enfermedades
from lugares.models import RecomendacionRutinas

admin.site.registe(Enfermedades)
admin.site.register(RecomendacionRutinas)