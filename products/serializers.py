from rest_framework import serializers
from .models import Store, Product


class StoreSerializer(serializers.ModelSerializer):
    """
    StoreSerilizer maps to the Store model
    """
    class Meta:
        model = Store
        exclude = ('products',)


class ProductSerializer(serializers.ModelSerializer):
    """
    ProductSerilizer maps to the Product model
    """
    class Meta:
        model = Product
        exclude = ('attributes', 'style', 'stores',)


class BeerSerializer(serializers.ModelSerializer):
    """
    BeerSerilizer maps to the Product model but only shows common information
    """
    class Meta:
        model = Product
        exclude = ('product_id', 'size', 'price', 'attributes', 'style', 'stores',)
