from django.db import models

# Create your models here.


class Product(models.Model):
    sku = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    brand = models.CharField(max_length=100)
    times_queried = models.IntegerField(default=0)

    def as_json(self):
        return dict(
            sku=self.sku,
            name=self.name,
            price=self.price,
            brand=self.brand,
            times_queried=self.times_queried)
