from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from .models import Store, Product


def _response(request, result, encoder=DjangoJSONEncoder):
    if request.GET.get('format', None) == 'html':
        output = '<table>'
        if isinstance(result, dict):
            for key, value in result.items():
                output += '<tr><th>%s</th><td>%s</td></tr>' % (key, value)
        elif isinstance(result, list):
            first_row = True
            for line in result:
                if first_row:
                    first_row = False
                    output += '<tr>'
                    for key, value in line.items():
                        output += '<th>%s</th>' % key
                    output += '</tr>'
                output += '<tr>'
                for key, value in line.items():
                    output += '<td>%s</td>' % value
                output += '</tr>'
        output += '</table>'
        return HttpResponse(output)

    return JsonResponse(result, safe=False, encoder=encoder)


def stores(request):
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
    return _response(request, list(stores.values()))


def store_by_id(request, store_id):
    """
    Returns data on a Beer Store location with a specified store id
    """
    # get store by id
    store = Store.objects.get(store_id = int(store_id))

    # return data
    return _response(request, model_to_dict(store))


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
    return _response(request, list(stores.values()))


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
    return _response(request, list(products.values()))


def product_by_id(request, product_id):
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
    return _response(request, model_to_dict(product), encoder=ProductEncoder)


def products_at_store(request, store_id):
    """
    Returns all products at a specified store
    category -- The products's category 
    type -- The product's type
    brewer -- The products's brewer
    country -- The product's country of origin
    on_sale -- If the product is on sale (true|false)
    size -- Size keyword
    """
    products = Product.objects.filter(stores__store_id=int(store_id))
    
    # get options
    category = request.GET.get('category', None)
    type = request.GET.get('type', None)
    brewer = request.GET.get('brewer', None)
    country = request.GET.get('country', None)
    on_sale = request.GET.get('on_sale', None)
    size = request.GET.get('size', None)

    # filter if options are set
    if category is not None:
        products = products.filter(category=category)
 
    if type is not None:
        products = products.filter(type=type)

    if brewer is not None:
        products = products.filter(brewer=brewer)

    if country is not None:
        products = products.filter(country=country)

    if size is not None:
        products = products.filter(size__icontains=size)

    if on_sale == "true":
        products = products.filter(on_sale=True)

    #return data
    return _response(request, list(products.values()))


def beer_products(request, beer_id):
    """
    Returns all products of a beer with a specified beer id
    """
    # get the beer's products
    products = Product.objects.filter(beer_id = int(beer_id))

    on_sale = request.GET.get('on_sale', None)
    
    if on_sale == "true":
        products = products.filter(on_sale=True)

    # return data
    return _response(request, list(products.values()))


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
    return _response(request, list(beers.values()))


def beer_by_id(request, beer_id):
    """
    Returns a beer with a specified beer id
    """
    # get beer
    beer = Product.objects.filter(beer_id = int(beer_id)).first()

    # return data
    return _response(request, model_to_dict(beer))
