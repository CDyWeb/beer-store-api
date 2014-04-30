from rest_framework import serializers
from .models import Store, Product, Inventory

class StoreSerializer(serializers.ModelSerializer):
    """
    StoreSerilizer maps to the Store model
    """
    #def get_pk_field(self, model_field):
    #    return None
        
    class Meta:
        model = Store


class ProductSerializer(serializers.ModelSerializer):
    """
    ProductSerilizer maps to the Product model
    """
    def get_pk_field(self, model_field):
        return None

    class Meta:
        model = Product
		

class ProductsAtStoreSerializer(serializers.ModelSerializer):
    """
    InventorySerilizer maps to the Inventory model
    """
    def get_pk_field(self, model_field):
        return None

    product = ProductSerializer()

    class Meta:
        model = Inventory
        exclude = ('store',)

class StoresWithProductSerializer(serializers.ModelSerializer):
    """
    InventorySerilizer maps to the Inventory model
    """
    def get_pk_field(self, model_field):
        return None

    store = StoreSerializer()

    class Meta:
        model = Inventory
        exclude = ('product',)
