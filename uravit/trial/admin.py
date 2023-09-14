from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Juicio)
admin.site.register(models.Victima)
admin.site.register(models.Testigo)
admin.site.register(models.Perito)
admin.site.register(models.ApoyoVictimaTraslado)