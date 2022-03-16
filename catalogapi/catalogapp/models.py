from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from catalogapi.auth.models import Notification


class Product(models.Model):
    sku = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    brand = models.CharField(max_length=100)
    times_queried = models.IntegerField(default=0)

    def queried(self):
        self.times_queried += 1
