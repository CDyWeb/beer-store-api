import json

from decimal import Decimal
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.http import JsonResponse
from .models import Store, Product


def stores(request, format=None):
    """
    Returns data on all Beer Store locations
    city -- The stores' city
    """
    stores = Store.objects.all()

    # get options
    city = request.GET.get('city', None)

    # filter if options are set
    if city is not None:
        stores = stores.filter(city=city)
    
    # return data
    return JsonResponse(list(stores.values()), safe=False)


def store_by_id(request, store_id, format=None):
    """
    Returns data on a Beer Store location with a specified store id
    """
    # get store by id
    store = Store.objects.get(store_id = int(store_id))

    # return data
    return JsonResponse(model_to_dict(store), safe=False)


def stores_with_product(request, product_id):
    """
    Returns all stores with a specified product
    city -- The stores' city
    """
    stores = Store.objects.filter(product__product_id=int(product_id))
    
    # get options
    city = request.GET.get('city', None)

    # filter if options are set
    if city is not None:
        stores = stores.filter(city=city)

    # return data
    return JsonResponse(list(stores.values()), safe=False)


def products(request):
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
    category = request.GET.get('category', None)
    type = request.GET.get('type', None)
    brewer = request.GET.get('brewer', None)
    country = request.GET.get('country', None)
    on_sale = request.GET.get('on_sale', None)

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
    return JsonResponse(list(products.values()), safe=False)


def product_by_id(request, product_id, format=None):
    """
    Returns data on a Beer Store product with a specified product id
    """
    # get product by id
    product = Product.objects.get(product_id = int(product_id))

    class ProductEncoder(DjangoJSONEncoder):
        def default(self, o):
            if isinstance(o, Store):
                return super().encode(model_to_dict(o))
            return super().default(o)

    # return data
    return JsonResponse(model_to_dict(product), safe=False, encoder=ProductEncoder)


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
    category = request.GET.get('category', None)
    type = request.GET.get('type', None)
    brewer = request.GET.get('brewer', None)
    country = request.GET.get('country', None)
    on_sale = request.GET.get('on_sale', None)

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
    return JsonResponse(list(products.values()), safe=False)


def beer_products(request, beer_id, format=None):
    """
    Returns all products of a beer with a specified beer id
    """
    # get the beer's products
    products = Product.objects.filter(beer_id = int(beer_id))

    on_sale = request.GET.get('on_sale', None)
    
    if on_sale == "true":
        products = products.filter(on_sale=True)

    # return data
    return JsonResponse(list(products.values()), safe=False)


def beers(request):
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
    category = request.GET.get('category', None)
    type = request.GET.get('type', None)
    brewer = request.GET.get('brewer', None)
    country = request.GET.get('country', None)
    on_sale = request.GET.get('on_sale', None)

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
    return JsonResponse(list(beers.values()), safe=False)


def beer_by_id(request, beer_id):
    """
    Returns a beer with a specified beer id
    """
    # get beer
    beer = Product.objects.filter(beer_id = int(beer_id)).first()

    # return data
    return JsonResponse(model_to_dict(beer), safe=False)
