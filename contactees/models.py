from django.db import models
from datetime import datetime

class Contactee(models.Model):
    listing = models.TextField(blank=False)
    listing_id = models.IntegerField()
    name = models.TextField(blank=False)
    email = models.TextField(blank=False)
    phone  = models.TextField(blank=False)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name
