from django.db import models

# Create your models here.


class TipoCuenta(models.Model):
    act_id = models.AutoField(primary_key=True)
    act_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    account_type = models.ForeignKey(
        TipoCuenta, models.DO_NOTHING, db_column='account_type')
    balance = models.IntegerField()
    iban = models.TextField()

    class Meta:
        managed = False
        db_table = 'cuenta'
