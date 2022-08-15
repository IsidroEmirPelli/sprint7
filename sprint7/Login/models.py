from django.db import models
from django.contrib.auth.models import User
from Clientes.models import Cliente
# Create your models here.

# one to one with cliente


class Usuario(User):
    customer = models.OneToOneField(
        Cliente, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
