from django.contrib import admin

# Register your models here.
from appstoretia.models import Ventas, Caracteristicas, Tiendas

admin.site.register(Ventas)
admin.site.register(Caracteristicas)
admin.site.register(Tiendas)