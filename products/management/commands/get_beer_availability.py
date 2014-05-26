# -*- coding: utf-8 -*-
import json
import urllib2
from django.core.management.base import BaseCommand
from django.template import Template, Context
from django.conf import settings
from lxml import etree
import pytz
from products.models import Store, Product
from url_settings import TOP_URL

class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        scrapes and stores product availability
        """
        # load all stores and 
        stores = Store.objects.all()
        products = Product.objects.all()

        # loop through products
        for product in products:
            
            # retrieve availability json
            data = json.load(urllib2.urlopen(TOP_URL+'/json/stores-with-sku/storelocations.bpid.%s.json' % (product.product_id,)))
            data = data['features']

            # create a list of stores to reduce amount of DB queries
            stores_to_add = []

            # loop through stores
            for d in data:
                store_id = d['properties']['storeid']

                # continue if store can't be found due to outdated data 
                # from the beer store site
                try:
                    store = stores.get(store_id=store_id)
                except:
                    continue
                
                # append to store list
                stores_to_add.append(store)

            # add stores where product is available
            product.stores.add(*stores_to_add)
