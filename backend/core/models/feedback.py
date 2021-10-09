from django.db import models
from .product import Product
import uuid

class Feedback(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    avaliation_text = models.CharField(max_length=200)
    avaliation = models.IntegerField(default=0)
    image = models.ImageField(upload_to='photos/product/feedback/%Y-%m-%d', blank=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return "%d (%s)" %(self.avaliation, self.avaliation_text)