from django.db import models
# Create your models here.


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    # Field name made lowercase.
    customer_dni = models.TextField(db_column='customer_DNI', unique=True)
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'cliente'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sucursal'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    # Field name made lowercase.
    employee_dni = models.TextField(db_column='employee_DNI')
    branch_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'empleado'


class Direcciones(models.Model):
    calle = models.TextField(primary_key=True)
    numero = models.IntegerField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()
    customer = models.ForeignKey(
        Cliente, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(
        'Empleado', models.DO_NOTHING, blank=True, null=True)
    branch = models.OneToOneField(
        'Sucursal', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'direcciones'


class Tiposclientes(models.Model):
    # Field name made lowercase.
    tipoid = models.AutoField(
        db_column='TipoId', primary_key=True, blank=True)
    name = models.TextField()

    class Meta:
        managed = True
        db_table = 'TiposClientes'
