from django.db import models
from django.conf import settings
# Create your models here.


class participant(models.Model):
    Pre = models.TextField()
    id = models.TextField(primary_key=True)
    Name = models.CharField(max_length=300)
    Email = models.CharField(max_length=300)
