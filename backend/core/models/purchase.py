from django.db import models
from .product import Product
from .user import User
import uuid

class Purchase(models.Model):
    class StatusCompra(models.IntegerChoices):
        cart = 1, 'Carrinho'
        made = 2, 'Realizado'
        paid  = 3, 'Pago'
        transit = 4, 'Em trânsito'
        delivered = 5, 'Entregue'

    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    value = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    protocol = models.CharField(max_length=200)
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.cart)
    products = models.ForeignKey(Product, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.protocol