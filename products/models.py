from django.db import models
from django.urls import reverse


class Store(models.Model):
    """
    Represents a Beer Store location
    """
    store_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True, default=None, blank=True)
    url = models.CharField(max_length=255, null=True, default=None, blank=True)
    address = models.CharField(max_length=255, null=True, default=None, blank=True)
    city = models.CharField(max_length=255, null=True, default=None, blank=True)
    postal_code = models.CharField(max_length=255, null=True, default=None, blank=True)
    phone = models.CharField(max_length=255, null=True, default=None, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, null=True, default=None, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=7, null=True, default=None, blank=True)
    monday_open = models.CharField(max_length=50, null=True, default=None, blank=True)
    monday_close = models.CharField(max_length=50, null=True, default=None, blank=True)
    tuesday_open = models.CharField(max_length=50, null=True, default=None, blank=True)
    tuesday_close = models.CharField(max_length=50, null=True, default=None, blank=True)
    wednesday_open = models.CharField(max_length=50, null=True, default=None, blank=True)
    wednesday_close = models.CharField(max_length=50, null=True, default=None, blank=True)
    thursday_open = models.CharField(max_length=50, null=True, default=None, blank=True)
    thursday_close = models.CharField(max_length=50, null=True, default=None, blank=True)
    friday_open = models.CharField(max_length=50, null=True, default=None, blank=True)
    friday_close = models.CharField(max_length=50, null=True, default=None, blank=True)
    saturday_open = models.CharField(max_length=50, null=True, default=None, blank=True)
    saturday_close = models.CharField(max_length=50, null=True, default=None, blank=True)
    sunday_open = models.CharField(max_length=50, null=True, default=None, blank=True)
    sunday_close = models.CharField(max_length=50, null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store_detail", kwargs={"store_id": self.store_id})


class Product(models.Model):
    """
    Represents a product at the beer store
    """
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    beer_id = models.IntegerField()
    image_url = models.URLField()
    category = models.CharField(max_length=255, default="N/A")
    abv = models.DecimalField(max_digits=3, decimal_places=1)
    style = models.CharField(max_length=255, default="N/A")
    attributes = models.CharField(max_length=255, default="N/A")
    type = models.CharField(max_length=255, default="N/A")
    brewer = models.CharField(max_length=255, default="N/A")
    country = models.CharField(max_length=255, default="N/A")
    on_sale = models.BooleanField(default=False)
    stores = models.ManyToManyField(Store, blank=True)

    def __unicode__(self):
        return self.name + " - " + self.size
