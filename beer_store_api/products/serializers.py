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
		

class ProductsAtStoreSerializer(serializers.ModelSerializer):
    """
    InventorySerilizer maps to the Inventory model
    """
    product = ProductSerializer(source='product')

    class Meta:
        model = Inventory
        exclude = ('store',)


class StoresWithProductSerializer(serializers.ModelSerializer):
    """
    InventorySerilizer maps to the Inventory model
    """
    store = StoreSerializer(source='store')

    class Meta:
        model = Inventory
        exclude = ('product',)


class InventorySerializer(serializers.ModelSerializer):
    """
    InventorySerilizer maps to the Inventory model
    """
    def get_pk_field(self, model_field):
         return None

    class Meta:
        model = Inventory


class BeerSerializer(serializers.ModelSerializer):
    """
    BeerSerilizer maps to the Product model
    """
    class Meta:
        model = Product
        exclude = ('product_id', 'size', 'price',)
	
