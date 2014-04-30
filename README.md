beer-store-api
==============

A REST web service that provides The Beer Store product, store, and inventory information. Not live yet, but here's the development code for anyone interested.

## Quick Start ##

### Stores ###
/stores

### Store ###
/store/{store_id}

### Inventory ###
/stores/{store_id}/products/{product_id}/inventory

## About ##
The Beer Store API collects and provides The Beer Store product, store, and inventory information. Currently, all data is served 
in padded JSON, but I'll probably include XML at some point. It'll probably be pretty basic initially, but I'll start including more info
and meta data as I continue working on it

## How it was made ##
- Python
- Django
- Django REST Framework
- Django REST Swagger (for documentation)
- Beautiful Soup (for scraping The Beer Store website)
