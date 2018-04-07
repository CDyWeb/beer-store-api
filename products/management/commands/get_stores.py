import json

import requests
from bs4 import BeautifulSoup
from products.models import Store
from django.core.management.base import BaseCommand
from .url_settings import TOP_URL


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        scrapes and stores store information
        """
        # get location json
        data = json.loads(requests.get(TOP_URL + '/storelocations.json').content.decode())
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
            link_soup = BeautifulSoup(link, "html.parser")
            store_link = link_soup.a['href']
            store_html = requests.get(TOP_URL + store_link).content

            # get store info
            store_soup = BeautifulSoup(store_html, "html.parser")
            brs = store_soup.find("div", "store-address-container").div.find_all('br')

            store_address = brs[0].previous_sibling
            store_city_postal = store_address.next_sibling.next_sibling
            store_phone = store_city_postal.next_sibling.next_sibling
            store_city = store_city_postal[:-8].split(",")[0]
            store_postal = store_city_postal[-7:]
            store_lat = coords[1]
            store_lng = coords[0]
            store_address = store_address.strip()

            # get hours
            try:
                store_table_hours = store_soup.find("table", "store-hours").tbody.find_all("tr")
                hours = []

                for store_hour in store_table_hours:
                    hours.append(store_hour.find_all("td")[1].get_text())
                    hours.append(store_hour.find_all("td")[2].get_text())
            # if store page is outdated (ie store doesn't exist) skip it
            except:
                continue

            # make a dictionary of date and hours
            days = ["monday-open", "monday-close",
                    "tuesday-open", "tuesday-close",
                    "wednesday-open", "wednesday-close",
                    "thursday-open", "thursday-close",
                    "friday-open", "friday-close",
                    "saturday-open", "saturday-close",
                    "sunday-open", "sunday-close"]
            store_hours = dict(zip(days, hours))

            # check if store exists
            # NOTE: used this custom solution because django get_or_create
            # doesn't play nice with custom primary keys
            try:
                store_entry = Store.objects.get(store_id=store_id)
                created = True
            except:
                store_entry = Store()
                created = False

            # if store doesn't exist set fields
            if not created:
                store_entry.store_id = int(store_id)
                store_entry.name = store_name.strip()
                store_entry.address = store_address.strip()
                store_entry.city = store_city.strip()
                store_entry.postal_code = store_postal.strip()
                store_entry.phone = store_phone.strip()
                store_entry.latitude = float(store_lat)
                store_entry.longitude = float(store_lng)

            # set hours
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

            # save store
            store_entry.save()
