from django.db import models
from utils.models import Register
from decimal import Decimal


class Product(Register):
    """
    Model that represent Products and Services
    """
    TYPE = (
        ('product', 'PRODUCTO'),
        ('service', 'SERVICIO')
    )
    
    code = models.CharField(verbose_name='Codigo', unique=True, max_length=20)
    name = models.CharField(verbose_name='Nombre', max_length=100, unique=True)
    value = models.DecimalField(verbose_name='Valor', max_digits=6, decimal_places=2,
                                default=Decimal('0.00'))
    type = models.CharField(verbose_name='Tipo', max_length=7, choices=TYPE, default='SERVICIO')

    def __str__(self):
        return self.name + ' | ' + str(self.value)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['code']

