from django.contrib import admin
from .models import *

# Register your models here.
# Esto es para mostrar los modelos creados en admin django web

admin.site.register(Productos)
admin.site.register(Contactos)