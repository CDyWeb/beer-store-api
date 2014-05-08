"""
Scrapes the beer store website and gets beer information
"""

import urllib2
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from django.template import Template, Context
from django.conf import settings
from settings import TOP_URL
from products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Gets product information
        """
        # this script hangs for some reason, temporary solution is
        # to curl the beers page in a cron job script
        #html = urllib2.urlopen(top_url + "/beers/search/all")

        # get beer page html and make soup object
        html = open("beers.html")
        soup_beers = BeautifulSoup(html)

        # find all beers
        beers = soup_beers.find_all("a", "brand-link")

        for beer in beers:
            # get beer page and make soup object
            beer_url = beer["href"]
            beer_html = urllib2.urlopen(TOP_URL + beer_url)
            soup_beer = BeautifulSoup(beer_html)

            # get sizes
            beer_types = soup_beer.find_all("table", "brand-pricing")

            # get propertis and valus and merge them into dict
            labels = soup_beer.dl.find_all("dt")
            details = soup_beer.dl.find_all("dd")
            beer_details = dict(zip(labels,details))

            # get name and image
            beer_name = soup_beer.find("h1", "page-title").get_text()
            beer_image = soup_beer.find("div","brand-image").img["src"]

            # loop through beer products
            for beer_type in beer_types:
                beer_sizes = beer_type.find("tbody").find_all("tr")

                for beer_size in beer_sizes:

                    # get product information
                    beer_size_attributes = beer_size.find_all("td")
                    beer_ids = beer_size.a["href"].split('=')[1]
                    beer_id = beer_ids.split('-')[0]
                    beer_product_id = beer_ids.split('-')[1]
                    
                    # Comment to disable monitoring
                    print "Beer Name: "+beer_name
                    print beer_size_attributes[0].get_text()
                    print beer_size_attributes[1].get_text()
                    print beer_id
                    print beer_product_id
                    print "Beer Image: "+beer_image
		
                    
                    product_entry, created = Product.objects.get_or_create(product_id=int(beer_product_id.strip()))

                    # make new product object if it doesnt exise
                    if not created:
                        product_entry.name = beer_name.strip()
                        product_entry.size = beer_size_attributes[0].get_text().strip()
                        product_entry.beer_id = int(beer_id.strip())
                        product_entry.product_id = int(beer_product_id.strip())
                        product_entry.image_url = beer_image.strip()
                        
                        for key, value in beer_details.iteritems():
                            attr = key.get_text()[:-1]
                            val = value.get_text()

                            print attr, val
				
                            if attr == 'Category':
                                product_entry.category = val
				
                            if attr == 'Alcohol Content (ABV)':
                                product_entry.abv = float(val[:-1])
					
                            if attr == 'Style':
                                product_entry.style= val

                            if attr == 'Attributes':
                                product_entry.attributes= val

                            if attr == 'Type':
                                product_entry.type= val

                            if attr == 'Brewer':
                                product_entry.brewer= val
			
                            if attr == 'Country':
                                product_entry.country = val

                    # update pricing info 
                    try:
			            product_entry.price = float(beer_size_attributes[1].get_text().strip()[1:])
                    except:
			            product_entry.price = float(beer_size_attributes[1].get_text().split('sale')[1].strip()[1:])
                    
                    # save product
                    product_entry.save()

                    print "*********************************************\n"
