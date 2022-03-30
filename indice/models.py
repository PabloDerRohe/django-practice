from django.db import models

# Create your models here.

class NuestroUser(models.Model)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    