from django.db import models

# Create your models here.


class Tipocuenta(models.Model):
    # Field name made lowercase.
    tipocuentaid = models.AutoField(
        db_column='tipoCuentaId', primary_key=True, blank=True)
    name = models.TextField()

    class Meta:
        managed = True
        db_table = 'TipoCuenta'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    # Field name made lowercase.
    tipocuentaid = models.ForeignKey(
        Tipocuenta, models.DO_NOTHING, db_column='tipoCuentaId')

    class Meta:
        managed = True
        db_table = 'cuenta'


class AuditoriaCuenta(models.Model):
    old_id = models.IntegerField()
    new_id = models.IntegerField()
    old_balance = models.IntegerField()
    new_balance = models.IntegerField()
    old_iban = models.TextField()
    new_iban = models.TextField()
    old_type = models.TextField()
    new_type = models.TextField()
    user_action = models.TextField()
    created_at = models.DateField()

    class Meta:
        managed = True
        db_table = 'Auditoria_Cuenta'


class Movimientos(models.Model):
    mov_id = models.AutoField(primary_key=True)
    nro_cuenta = models.ForeignKey(
        'Cuenta', models.DO_NOTHING, db_column='nro_cuenta')
    monto = models.IntegerField()
    op_type = models.TextField()
    hora = models.DateField()

    class Meta:
        managed = True
        db_table = 'Movimientos'
