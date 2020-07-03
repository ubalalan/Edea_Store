from django.db import models
from datetime import datetime
# Create your models here.

class Accounting(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title