from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from .models import Store, Product 
from .serializers import StoreSerializer, ProductSerializer, BeerSerializer


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
def stores_with_product(request, product_id):
    """
    Returns all stores with a specified product
    city -- The stores' city
    """
    stores = Store.objects.filter(product__product_id=int(product_id))
    
    # get options
    city = request.QUERY_PARAMS.get('city', None)

    # filter if options are set
    if city is not None:
        stores = stores.filter(city=city)

    # return data
    serializer = StoreSerializer(stores)
    return Response(serializer.data)


@api_view(['GET'])
def products(request, format=None):
    """
    Returns data on all Beer Store products
    category -- The products's category 
    type -- The product's type
    brewer -- The products's brewer
    country -- The product's country of origin
    on_sale -- If the product is on sale (true|false)
    """
    products = Product.objects.all()

    # get options
    category = request.QUERY_PARAMS.get('category', None)
    type = request.QUERY_PARAMS.get('type', None)
    brewer = request.QUERY_PARAMS.get('brewer', None)
    country = request.QUERY_PARAMS.get('country', None)
    on_sale = request.QUERY_PARAMS.get('on_sale', None)

    # filter if options are set
    if category is not None:
        products = products.filter(category=category)
 
    if type is not None:
        products = products.filter(type=type)

    if brewer is not None:
        products = products.filter(brewer=brewer)

    if country is not None:
        products = products.filter(country=country)

    if on_sale == "true":
        products = products.filter(on_sale=True)
 
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
def products_at_store(request, store_id):
    """
    Returns all products at a specified store
    category -- The products's category 
    type -- The product's type
    brewer -- The products's brewer
    country -- The product's country of origin
    on_sale -- If the product is on sale (true|false)
    """
    products = Product.objects.filter(stores__store_id=int(store_id))
    
    # get options
    category = request.QUERY_PARAMS.get('category', None)
    type = request.QUERY_PARAMS.get('type', None)
    brewer = request.QUERY_PARAMS.get('brewer', None)
    country = request.QUERY_PARAMS.get('country', None)
    on_sale = request.QUERY_PARAMS.get('on_sale', None)

    # filter if options are set
    if category is not None:
        products = products.filter(category=category)
 
    if type is not None:
        products = products.filter(type=type)

    if brewer is not None:
        products = products.filter(brewer=brewer)

    if country is not None:
        products = products.filter(country=country)

    if on_sale == "true":
        products = products.filter(on_sale=True)

    #return data
    serializer = ProductSerializer(products)
    return Response(serializer.data)


@api_view(['GET'])
def beer_products(request, beer_id, format=None):
    """
    Returns all products of a beer with a specified beer id
    """
    # get the beer's products
    products = Product.objects.filter(beer_id = int(beer_id))

    # return data
    serializer = ProductSerializer(products)
    return Response(serializer.data)


@api_view(['GET'])
def beers(request, format=None):
    """
    Returns all beers
    category -- The beer's category 
    type -- The beer's type
    brewer -- The beer's brewer
    country -- The beer's country of origin
    on_sale -- If at least one of the beer's products is on sale (true|false)
    """
    beers = Product.objects.distinct('beer_id')
    
    # get options
    category = request.QUERY_PARAMS.get('category', None)
    type = request.QUERY_PARAMS.get('type', None)
    brewer = request.QUERY_PARAMS.get('brewer', None)
    country = request.QUERY_PARAMS.get('country', None)
    on_sale = request.QUERY_PARAMS.get('on_sale', None)

    # filter if options are set
    if category is not None:
        beers = beers.filter(category=category)
 
    if type is not None:
        beers = beers.filter(type=type)

    if brewer is not None:
        beers = beers.filter(brewer=brewer)

    if country is not None:
        beers = beers.filter(country=country)

    if on_sale == "true":
        beers = beers.filter(on_sale=True)

    # return data
    serializer = BeerSerializer(beers)
    return Response(serializer.data)


@api_view(['GET'])
def beer_by_id(request, beer_id, format=None):
    """
    Returns a beer with a specified beer id
    """
    # get beer
    beer = Product.objects.filter(beer_id = int(beer_id)).distinct('beer_id')

    # return data
    serializer = BeerSerializer(beer)
    return Response(serializer.data)
