from django.db import models
from .category import Category
import uuid

class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    sku = models.IntegerField(default=0)
    value = models.FloatField(default=0)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='photos/product/%Y-%m-%d', blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name