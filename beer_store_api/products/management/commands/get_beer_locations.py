# -*- coding: utf-8 -*-
import json
import urllib2
from datetime import datetime
from django.core.management.base import BaseCommand
from django.template import Template, Context
from django.conf import settings
import pytz
from bs4 import BeautifulSoup
from settings import TOP_URL
from products.models import Store, Product, Inventory


def get_beer_locations(product_id, beer_id, size):
    """
    Gets beer inventory information
    """
    # get basic store json from beer store website
    data = json.load(urllib2.urlopen(TOP_URL+'/json/stores-with-sku/storelocations.bpid.%s.json' % (product_id,)))
    data = data['features']

    # get product
    product = Product.objects.get(product_id=product_id)

    for d in data:

        # get store object
        store_id = d['properties']['storeid']
        store = Store.objects.get(store_id=store_id)
        print beer_id

        # get product at store information
        beer_html = urllib2.urlopen(TOP_URL+'/beers/inventory/%s/%s' % (beer_id ,store_id))
        soup_beer = BeautifulSoup(beer_html)
        print store_id
        beers = soup_beer.find("table","brand-pricing")
        beer = beers.find("td", text=size)
        print beer.get_text()

        # get quantity
        quantity = beer.next_sibling.next_sibling.get_text()
        print quantity

        inventory, created = Inventory.objects.get_or_create(product=product, store=store)

        # create new inventory object if it doesnt exist
        if not created:
            inventory.product = product
            inventory.store = store

        # update quantity and last updated date
        inventory.quantity = int(quantity)
        inventory.last_updated = datetime.utcnow().replace(tzinfo=pytz.utc)

        # save
        inventory.save()
        print "*******************************************"


class Command(BaseCommand):
    def handle(self, *args, **options):
    """
    Inventory management command
    """
        for product in Product.objects.all():
            get_beer_locations(product.product_id, product.beer_id, product.size)
