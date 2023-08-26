from django.db import models

# Create your models here.

class Password(models.Model):
    name = models.TextField()
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)