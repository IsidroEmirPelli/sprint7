from django.db import models
from Clientes.models import Cliente
# Create your models here.


class Marcatarjeta(models.Model):
    # Field name made lowercase.
    marcaid = models.AutoField(
        db_column='MarcaId', primary_key=True, blank=True)
    name = models.TextField()

    class Meta:
        managed = True
        db_table = 'MarcaTarjeta'


class Tarjeta(models.Model):
    # Field name made lowercase.
    numerotarjeta = models.AutoField(
        db_column='NumeroTarjeta', primary_key=True)
    # Field name made lowercase.
    cvv = models.IntegerField(db_column='CVV', blank=True, null=True)
    fecha_de_otorgamiento = models.DateField()
    fecha_de_expiracion = models.DateField()
    tipo_tarjeta = models.TextField()
    # Field name made lowercase.
    marcaid = models.ForeignKey(
        Marcatarjeta, models.DO_NOTHING, db_column='marcaId')
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'tarjeta'
