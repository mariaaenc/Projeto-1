from django.db import models
import uuid

class Category(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/category/%Y-%m-%d', blank=True)

    def __str__(self):
        return self.name