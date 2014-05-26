beer-store-api
==============

A REST web service that provides The Beer Store product, store, and inventory information. Not live yet, but here's the development code for anyone interested.

## About ##
The Beer Store API is a free to use REST service that provides 
The Beer Store store, product, and availability information. The service 
periodically crawls The Beer Store website to collect data and serves padded JSON. 
This service has no official association with The Beer Store.

The Beer Store API is a side project, so I'll try to implement features when 
I get the chance. As of now, the data is pretty basic (ie. no meta data, no pagination), 
but should be enough to make some cool applications. I've tried to make sure the data is 
accurate as possible, but unfortunately I'm limited to the accuracy of The Beer Store website. 
For example, you'll notice that there's a store with coordinates that place it in the Atlantic Ocean 
just west of Africa. That's just what I scraped from the website.

## How it was made ##
- Python
- Django
- Django REST Framework
- Django REST Swagger (for documentation)
- Beautiful Soup (for scraping The Beer Store website)
