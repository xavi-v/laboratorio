from django.db import models

# Create your models here.
class Laboratorio(models.Model):
    nombre = models.CharField(max_length = 256)
    ciudad = models.CharField(max_length=256, default="")
    pais = models.CharField(max_length=256, blank=True, null=True)
    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length = 256)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.PROTECT)
    especialidad = models.CharField(max_length=256, default="")

class Producto(models.Model):
    # id unico , siempre el id unico
    nombre = models.CharField(max_length = 256, unique = True)
    laboratorio = models.ForeignKey(Laboratorio, on_delete = models.PROTECT)
    f_fabricacion = models.DateField()
    p_costo = models.DecimalField(decimal_places = 2, max_digits = 12)
    p_venta = models.DecimalField(decimal_places = 2, max_digits = 12)
    # 1234567890.33