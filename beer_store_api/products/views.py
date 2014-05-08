from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from .models import Store, Product, Inventory 
from .serializers import StoreSerializer, ProductSerializer, StoresWithProductSerializer, ProductsAtStoreSerializer, InventorySerializer, BeerSerializer


# Store Views
@api_view(['GET'])
def stores(request, format=None):
    """
    Returns data on all Beer Store locations
    city -- The stores' city
    """
    stores = Store.objects.all()

    # get options
    city = request.QUERY_PARAMS.get('city', None)

    # filter if options are set
    if city is not None:
        stores = stores.filter(city=city)
    
    # return data
    serializer = StoreSerializer(stores)
    return Response(serializer.data)


@api_view(['GET'])
def store_by_id(request, store_id, format=None):
    """
    Returns data on a Beer Store location with a specified store id
    """
    # get store by id
    stores = Store.objects.get(store_id = int(store_id))

    # return data
    serializer = StoreSerializer(stores)
    return Response(serializer.data)


@api_view(['GET'])
def stores_with_product(request, product_id, format=None):
    """
    Returns stores with a specified product
    """
    # get product by id
    product = Product.objects.get(product_id=int(product_id))

    # get inventory quantities
    inventory = Inventory.objects.filter(product=product)

    # return data
    serializer = StoresWithProductSerializer(inventory)
    return Response(serializer.data)


# Product Views
@api_view(['GET'])
def products(request, format=None):
    """
    Returns data on all Beer Store products
    category -- The beer's category 
    type -- The beer's type
    brewer -- The beer's brewer
    country -- The beer's country of origin
    """
    products = Product.objects.all()

    # get options
    category = request.QUERY_PARAMS.get('category', None)
    type = request.QUERY_PARAMS.get('type', None)
    brewer = request.QUERY_PARAMS.get('brewer', None)
    country = request.QUERY_PARAMS.get('country', None)

    # filter if options are set
    if category is not None:
        products = products.filter(category=category)
 
    if type is not None:
        products = products.filter(type=type)

    if brewer is not None:
        products = products.filter(brewer=brewer)

    if country is not None:
        products = products.filter(country=country)
 
    # return data
    serializer = ProductSerializer(products)
    return Response(serializer.data)


@api_view(['GET'])
def product_by_id(request, product_id, format=None):
    """
    Returns data on a Beer Store product with a specified product id
    """
    # get product by id
    product = Product.objects.get(product_id = int(product_id))

    # return data
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def products_at_store(request, store_id, format=None):
    """
    Returns products at a specified store
    """
    # get store by id
    store = Store.objects.get(store_id=int(store_id))

    # get inventory quantity
    inventory = Inventory.objects.filter(store=store)

    # return data
    serializer = ProductsAtStoreSerializer(inventory)
    return Response(serializer.data)


# Inventory Views
@api_view(['GET'])
def inventory(request, store_id, product_id, format=None):
    """
    Returns inventory of a specified product at specified store
    """
    # get store and product by id
    store = Store.objects.get(store_id=int(store_id))
    product = Product.objects.get(product_id=int(product_id))

    # get product inventory
    inventory = Inventory.objects.get(store=store, product=product)

    # return data
    serializer = InventorySerializer(inventory)
    return Response(serializer.data)


@api_view(['GET'])
def inventories(request, format=None):
    """
    Returns all inventories
    """
    inventory = Inventory.objects.all()

    serializer = InventorySerializer(inventory)
    return Response(serializer.data)


@api_view(['GET'])
def product_inventories(request, product_id, format=None):
    """
    Returns all inventories of a specified product
    """
    product = Product.objects.get(product_id=int(product_id))
    inventory = Inventory.objects.filter(product=product)

    serializer = InventorySerializer(inventory)
    return Response(serializer.data)


@api_view(['GET'])
def beers(request, format=None):
    """
    Returns all beers
    """
    beers = Product.objects.distinct('beer_id')
    serializer = BeerSerializer(beers)
    return Response(serializer.data)


@api_view(['GET'])
def beer_by_id(request, beer_id, format=None):
    """
    Returns a beer with a specified beer id
    """
    beer = Product.objects.filter(beer_id = int(beer_id)).distinct('beer_id')
    serializer = BeerSerializer(beer)
    return Response(serializer.data)


@api_view(['GET'])
def beer_products(request, beer_id, format=None):
    """
    Returns a beer with a specified beer id
    """
    beers = Product.objects.filter(beer_id = int(beer_id))
    serializer = ProductSerializer(beers)
    return Response(serializer.data)
