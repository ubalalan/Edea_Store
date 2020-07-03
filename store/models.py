from django.db import models
from datetime import datetime

# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
