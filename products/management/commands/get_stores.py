import json
from time import sleep

import requests
from products.models import Store
from django.core.management.base import BaseCommand
from .url_settings import TOP_URL
import re
import logging

log = logging.getLogger(__name__)

class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        scrapes and stores store information
        """
        session = requests.session()
        session.headers = {
            'Accept': '*/*',
            'User-Agent': 'curl/7.54.0',
        }
        ajax_url = TOP_URL + '/wp-admin/admin-ajax.php'
        pageno = 0

        # start server session
        session.get(TOP_URL).raise_for_status()

        while True:
            pageno += 1
            response = session.post(
                url=ajax_url,
                data=f'action=store_top_five_nearest_store&sid=&pageno={pageno}&postcode_city=&locateme=&current_lat=&current_long=',
                headers={
                    'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
                },
                allow_redirects=False
            )
            response.raise_for_status()
            payload = response.content.decode()
            data = json.loads(payload)
            log.debug(data)

            if len(data) == 0:
                break

            for element in data:
                try:
                    store_entry = Store.objects.get(store_id=element['store_id'])
                    store_entry.name = element['store_name']
                except Store.DoesNotExist:
                    store_entry = Store.objects.create(store_id=element['store_id'], name=element['store_name'])

                store_entry.latitude = element['store_lat'] or None
                store_entry.longitude = element['store_long'] or None
                match = re.search('^(.+), (\w{6})$', element['address'])
                if match:
                    store_entry.address = match.group(1)
                    store_entry.postal_code = match.group(2)
                else:
                    store_entry.address = element['address']
                store_entry.url = element['url']

                hours = json.loads(element['fullhours'])
                for i, d in enumerate(['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']):
                    setattr(store_entry, f'{d}_open', hours[i][0])
                    setattr(store_entry, f'{d}_close', hours[i][1])

                store_entry.save()

            sleep(3)
