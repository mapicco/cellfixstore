from django.db import models
from utils.models import Register


class Client(Register):
    """
    Model that represent Clients
    """
    identification = models.CharField(verbose_name="DNI", max_length=13, unique=True)
    name = models.CharField(verbose_name="Nombre", max_length=200, default='')
    surname = models.CharField(verbose_name="Apellido", max_length=200, default='')
    email = models.EmailField(verbose_name="Email", unique=True)
    phone = models.CharField(verbose_name="Telefono", max_length=100)
    address = models.CharField(verbose_name="Direccion", max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['name']

