from django.db import models

class Producto (models.Model):
    id_producto = models.BigAutoField(primary_key=True)
    precio = models.IntegerField(verbose_name='Precio')
    tipo_producto = models.CharField( max_length=255,verbose_name='Tipo de producto')
    

    def __str__(self):
        return self.tipo_producto

class Cliente(models.Model):
    id_cliente = models.BigAutoField(primary_key=True)
    carnet_id = models.CharField(max_length=11, verbose_name='Carnet de Identidad', unique=True)
    numero_telefono = models.CharField(max_length=8, verbose_name='Número de telefóno')
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    producto = models.ForeignKey(Producto, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        
    def __str__(self):
        return self.nombre
