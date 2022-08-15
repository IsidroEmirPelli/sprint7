# Generated by Django 4.1 on 2022-08-15 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cuenta",
            fields=[
                ("account_id", models.AutoField(primary_key=True, serialize=False)),
                ("customer_id", models.IntegerField()),
                ("balance", models.IntegerField()),
                ("iban", models.TextField()),
            ],
            options={
                "db_table": "cuenta",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="TipoCuenta",
            fields=[
                ("act_id", models.AutoField(primary_key=True, serialize=False)),
                ("act_name", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "tipo_cuenta",
                "managed": False,
            },
        ),
    ]