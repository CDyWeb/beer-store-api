"""
Scrapes the beer store website and gets beer information
"""

import urllib2
from bs4 import BeautifulSoup
from settings import TOP_URL
from products.models import Product

# THIS IS A PROBLEM BUT I DONT KNOW WHY
# I GUESS ILL JUST DOWNLOAD THE HTML AND THEN OPEN IT
html = urllib2.urlopen(TOP_URL + "/beers/search/all")

# THIS WORKS THOUGH...WHY? 
#html = open("../pages/beers.html")

soup_beers = BeautifulSoup(html)

beers = soup_beers.find_all("a", "brand-link")

for beer in beers:
	beer_url = beer["href"]
	beer_html = urllib2.urlopen(TOP_URL + beer_url)
	soup_beer = BeautifulSoup(beer_html)
	beer_types = soup_beer.find_all("table", "brand-pricing")
	labels = soup_beer.dl.find_all("dt")
	details = soup_beer.dl.find_all("dd")
	beer_name = soup_beer.find("h1", "page-title").get_text()
	beer_image = soup_beer.find("div","brand-image").img["src"]
	beer_details = dict(zip(labels,details))

	for beer_type in beer_types:
		beer_sizes = beer_type.find("tbody").find_all("tr")

		for beer_size in beer_sizes:
			print "Beer Name: "+beer_name
			beer_size_attributes = beer_size.find_all("td")
			print beer_size_attributes[0].get_text()
			print beer_size_attributes[1].get_text()
			beer_ids = beer_size.a["href"].split('=')[1]
			beer_id = beer_ids.split('-')[0]
			beer_product_id = beer_ids.split('-')[1]
			print beer_id
			print beer_product_id
			
			print "Beer Image: "+beer_image

			
			product_entry = Product()
			product_entry.name = beer_name.strip()
			product_entry.size = beer_size_attributes[0].get_text().strip()
			product_entry.price = float(beer_size_attributes[1].get_text().strip()[1:])
			product_entry.beer_id = int(beer_id.strip())
			product_entry.product_id = int(beer_product_id.strip())
			product_entry.image_url = beer_image.strip()

			options = {
			              'Category': product_entry.category,
			              'Alcohol Content (ABV)': product_entry.abv,
			              'Style': product_entry.style,
			              'Attributes': product_entry.attributes,
			              'Type': product_entry.type,
			              'Brewer': product_entry.brewer,
			              'Country': product_entry.country
					  }
		
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

			product_entry.save()

			print "*********************************************\n"
