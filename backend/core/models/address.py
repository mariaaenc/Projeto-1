from django.db import models
from .user import User

class Address(models.Model):
    class Meta:
        verbose_name = "address"
        verbose_name_plural = "adresses"

    description = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    state_code = models.CharField(max_length=4)
    country = models.CharField(max_length=200)
    country_code= models.CharField(max_length=4)
    number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return self.description