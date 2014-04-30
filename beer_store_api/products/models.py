from django.core.urlresolvers import reverse
from django.db import models

class Store(models.Model):
	"""
	Represents a Beer Store location
	"""
	name = models.CharField(max_length=255)
	store_id = models.IntegerField(unique=True)
	address = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	postal_code = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	latitude = models.DecimalField(max_digits=9, decimal_places=7)
	longitude = models.DecimalField(max_digits=9, decimal_places=7)
	monday_open = models.CharField(max_length=50)
	monday_close = models.CharField(max_length=50)
	tuesday_open = models.CharField(max_length=50)
	tuesday_close = models.CharField(max_length=50)
	wednesday_open = models.CharField(max_length=50)
	wednesday_close = models.CharField(max_length=50)
	thursday_open = models.CharField(max_length=50)
	thursday_close = models.CharField(max_length=50)
	friday_open = models.CharField(max_length=50)
	friday_close = models.CharField(max_length=50)
	saturday_open = models.CharField(max_length=50)
	saturday_close = models.CharField(max_length=50)
	sunday_open = models.CharField(max_length=50)
	sunday_close = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse("store_detail", kwargs={"store_id": self.store_id})

class Product(models.Model):
	"""
	Represents a product at the beer store
	"""
	name = models.CharField(max_length=255)
	size = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	beer_id = models.IntegerField()
	product_id = models.IntegerField(unique=True)
	image_url = models.URLField()
	category = models.CharField(max_length=255, default="N/A")
	abv = models.DecimalField(max_digits=3, decimal_places=1)
	style = models.CharField(max_length=255, default="N/A")
	attributes = models.CharField(max_length=255, default="N/A")
	type = models.CharField(max_length=255, default="N/A")
	brewer = models.CharField(max_length=255, default="N/A")
	country = models.CharField(max_length=255, default="N/A")

	def __unicode__(self):
		return self.name + " - " + self.size

class Inventory(models.Model):
	"""
	Represents product inventories
	"""
	product = models.ForeignKey(Product)
	store = models.ForeignKey(Store)
	quantity = models.IntegerField()

	def __unicode__(self):
		return self.quantity
	
