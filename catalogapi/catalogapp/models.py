from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Product(models.Model):
    sku = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    brand = models.CharField(max_length=100)
    times_queried = models.IntegerField(default=0)

    def queried(self):
        self.times_queried += 1


class Notification(models.Model):
    text = models.CharField(max_length=100)


@receiver(post_save, sender=Product)
def save_comment(sender, instance, created, **kwargs):
    if created == False:
        Notification.objects.create(
            text='product with sku: ' + str(instance.sku) + ' has been updated')
