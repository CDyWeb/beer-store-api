import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from products.models import Product
from .url_settings import TOP_URL


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Scrapes and stores product information
        """
        # get beer page html and make soup object
        html = requests.get(TOP_URL + "/beers/search").content
        soup_beers = BeautifulSoup(html, "html.parser")

        # find all beers
        beers = soup_beers.find_all("a", "brand-link")

        for beer in beers:
            # get beer page and make soup object
            beer_url = beer["href"]
            beer_html = requests.get(TOP_URL + beer_url).content
            soup_beer = BeautifulSoup(beer_html, "html.parser")

            # get sizes
            beer_products = soup_beer.find_all("table", "brand-pricing")

            # get propertis and valus and merge them into dict
            labels = soup_beer.dl.find_all("dt")
            details = soup_beer.dl.find_all("dd")
            beer_details = dict(zip(labels, details))

            # get name and image
            beer_name = soup_beer.find("div", "only-desktop").find("h1", "page-title").get_text()
            beer_image = soup_beer.find("div","brand-image").img["src"]

            # get country and type
            beer_attributes = soup_beer.find("p","introduction").find_all("span")
            beer_attributes = beer_attributes[::-1]
            beer_country =  beer_attributes[0].get_text()
            beer_type = beer_attributes[1].get_text()

            # loop through beer products
            for beer_product in beer_products:
                beer_containers = beer_product.find_all("tbody")

                # loop through container tables
                for beer_container in beer_containers:
                    beer_sizes = beer_container.find_all("tr")

                    # loop through container sizes
                    for beer_size in beer_sizes:

                        # get product information
                        beer_ids = beer_size.a["href"].split('=')[1]
                        beer_id = beer_ids.split('-')[0]
                        # print beer_id
                        beer_product_id = beer_ids.split('-')[1]
                    
                        # Comment to disable monitoring
                        beer_product_size = beer_size.find("td", "size").get_text()
                        beer_product_price =  beer_size.find("td", "price").get_text()
                    
                        # check if product exists
                        # NOTE: used this custom solution because django get_or_create
                        # doesn't play nice with custom primary keys
                        try:
                            product_entry = Product.objects.get(product_id=int(beer_product_id.strip()))
                        except: 
                            product_entry = Product()

                        # set fields
                        product_entry.name = beer_name.strip()
                        product_entry.size = beer_product_size.strip()
                        product_entry.beer_id = int(beer_id.strip())
                        product_entry.product_id = int(beer_product_id.strip())
                        product_entry.image_url = beer_image.strip()
                        product_entry.country = beer_country.strip()
                        product_entry.type = beer_type.strip()
                        
                        # set product attributes
                        # NOTE: this code was created befor the beer store redesign
                        # it still works but some items no longer exist so they were 
                        # temporarily omitted from the serializer
                        for key, value in beer_details.items():
                            attr = key.get_text()[:-1]
                            val = value.get_text()

                            if attr == 'Category':
                                product_entry.category = val

                            if attr == 'Alcohol Content (ABV)':
                                product_entry.abv = float(val[:-1])

                            if attr == 'Style':
                                product_entry.style= val

                            if attr == 'Attributes':
                                product_entry.attributes= val

                            if attr == 'Brewer':
                                product_entry.brewer= val
            

                        # update pricing info 
                        try:
                            product_entry.price = float(beer_product_price.strip()[1:])
                            product_entry.on_sale = False
                        
                        except:
                            product_entry.price = float(beer_product_price.split('sale')[1].strip()[1:])
                            product_entry.on_sale = True

                        product_entry.save()
