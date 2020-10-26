from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.TextField(blank=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.TextField(blank=False)
    email = models.TextField(blank=False) 
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):

        return self.name
