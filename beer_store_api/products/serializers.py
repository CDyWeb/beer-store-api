from rest_framework import serializers
from .models import Store, Product, Inventory

class StoreSerializer(serializers.ModelSerializer):
	"""
	StoreSerilizer maps to the Store model
	"""
	class Meta:
		model = Store


class ProductSerializer(serializers.ModelSerializer):
	"""
	ProductSerilizer maps to the Product model
	"""
	class Meta:
		model = Product
		

class InventorySerializer(serializers.ModelSerializer):
	"""
	InventorySerilizer maps to the Inventory model
	"""
	class Meta:
		model = Inventory
