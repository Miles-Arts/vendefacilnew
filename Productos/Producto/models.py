from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    peso = models.PositiveBigIntegerField()
    caracteristicas = models.CharField(max_length=300, default="Sin características")
    foto = models.ImageField(upload_to='productos/', null=False, blank=False, default='productos/default.jpg')
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.peso)


