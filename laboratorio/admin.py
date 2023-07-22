from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto


@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
	list_display = ("id", "nombre")


# Register your models here.

@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
	list_display = ("id", "nombre", "laboratorio")


# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
	list_display = ("id", "nombre", "laboratorio", "year", "p_costo", "p_venta")

	def year(self, obj):
		return obj.f_fabricacion.strftime("%Y") #debe ser con Y mayuscula
												## para que muestre el años entero "ej 2020 y no 20"