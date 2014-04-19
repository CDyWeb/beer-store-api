from rest_framework import serializers
from .models import Store, Inventory

class StoreSerializer(serializers.ModelSerializer):
	"""
	StoreSerilizer maps to the Store model
	"""
	class Meta:
		model = Store

class InventorySerializer(serializers.ModelSerializer):
	"""
	InventorySerilizer maps to the Inventory model
	"""
	class Meta:
		model = Inventory
