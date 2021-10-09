from django.db import models
from django.contrib.auth.models import User
import uuid

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/user/%Y-%m-%d', blank=True)
    cpf_cnpj = models.CharField(max_length=25)
    email = models.EmailField()
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
