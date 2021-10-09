from django.db import models
from .category import Category
import uuid

class SubCategory(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/category/subcategory/%Y-%m-%d', blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return "%s (%s)" %(self.name, self.category)