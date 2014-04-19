# -*- coding: utf-8 -*-
import json
import urllib2
from bs4 import BeautifulSoup
from settings import TOP_URL
from products.models import Store, Product, Inventory

"""
get_beer_locations retrieves store information using json served by the beer store website
"""

def get_beer_locations(product_id, beer_id, size):
	data = json.load(urllib2.urlopen(TOP_URL+'/json/stores-with-sku/storelocations.bpid.%s.json' % (product_id,)))
	data = data['features']
	product = Product.objects.get(product_id=product_id)

	for d in data:
		store_id = d['properties']['storeid']
		store = Store.objects.get(store_id=store_id)
		print beer_id
		beer_html = urllib2.urlopen(TOP_URL+'/beers/inventory/%s/%s' % (beer_id ,store_id))
		soup_beer = BeautifulSoup(beer_html)
		print store_id
		beers = soup_beer.find("table","brand-pricing")
		beer = beers.find("td", text=size)
		print beer.get_text()

		quantity = beer.next_sibling.next_sibling.get_text()
		print quantity

		inventory = Inventory()

		inventory.product_id = product
		inventory.store_id = store
		inventory.quantity = int(quantity)
		inventory.save()

		print "*******************************************"

for product in Product.objects.all():
	get_beer_locations(product.product_id, product.beer_id, product.size)
