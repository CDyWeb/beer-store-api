"""
Retrieves store information using json served by the beer store website
"""

import json
import urllib2
from bs4 import BeautifulSoup
from settings import TOP_URL
from products.models import Store

# get location json
data = json.load(urllib2.urlopen(TOP_URL+'/storelocations.json'))
data = data['features']

# loop through each location
for d in data:
	
	# get json properties
	store = d['properties']
	coords = d['geometry']['coordinates']
	store_name = store['name']
	store_id = store['storeid']
	link = store['description']

	# go to store page
	link_soup = BeautifulSoup(link)
	store_link = link_soup.a['href']
	store_html = urllib2.urlopen(TOP_URL+store_link)

	store_soup = BeautifulSoup(store_html)
	store_address = store_soup.find("div", "content-address").div.h3.next_sibling
	store_city_postal = store_address.next_sibling.next_sibling
	store_phone = store_city_postal.next_sibling.next_sibling
	store_city = store_city_postal[:-8].split(",")[0]
	store_postal = store_city_postal[-7:]
	store_lat = coords[0]
	store_lng = coords[1]
	store_address = store_address.strip()

	print "Name: "+store_name
	print "ID: "+str(store_id)
	print "Link: "+store_link
	print "Address: "+store_address
	print "City: "+store_city
	print "Postal: "+store_postal
	print "Phone: "+store_phone
	print "Latitude: "+str(store_lat)
	print "Longitude: "+str(store_lng)

	try:
		store_table_hours = store_soup.find("table", "store-hours").tbody.find_all("tr")
		hours = []

		for store_hour in store_table_hours:
			hours.append(store_hour.find_all("td")[1].get_text())
			hours.append(store_hour.find_all("td")[2].get_text())

	except:
		continue

	days = ["monday-open", "monday-close", 
	        "tuesday-open", "tuesday-close", 
			"wednesday-open", "wednesday-close",
	        "thursday-open", "thursday-close",
	        "friday-open", "friday-close",
	        "saturday-open", "saturday-close",
	        "sunday-open", "sunday-close"]
	
	store_hours = dict(zip(days, hours))

	for key, value in store_hours.iteritems():
		print key+ ": "+value
	
	store_entry = Store()
	store_entry.name = store_name.strip()
	store_entry.store_id = int(store_id)
	store_entry.address = store_address.strip()
	store_entry.city = store_city.strip()
	store_entry.postal_code = store_postal.strip()
	store_entry.phone = store_phone.strip()
	store_entry.latitude = float(store_lat)
	store_entry.longitude = float(store_lng)
	store_entry.monday_open = store_hours["monday-open"]
	store_entry.monday_close = store_hours["monday-close"]
	store_entry.tuesday_open = store_hours["tuesday-open"]
	store_entry.tuesday_close = store_hours["tuesday-close"]
	store_entry.wednesday_open = store_hours["wednesday-open"]
	store_entry.wednesday_close = store_hours["wednesday-close"]
	store_entry.thursday_open = store_hours["thursday-open"]
	store_entry.thursday_close = store_hours["thursday-close"]
	store_entry.friday_open = store_hours["friday-open"]
	store_entry.friday_close = store_hours["friday-close"]
	store_entry.saturday_open = store_hours["saturday-open"]
	store_entry.saturday_close = store_hours["saturday-close"]
	store_entry.sunday_open = store_hours["sunday-open"]
	store_entry.sunday_close = store_hours["sunday-close"]
	store_entry.save()

	print "***********************************************************\n"
