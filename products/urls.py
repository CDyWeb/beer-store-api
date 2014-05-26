from django.conf.urls import patterns, url
from products import views

urlpatterns = patterns("",

	# /stores
	url(
		regex=r"^stores/$",
		view=views.stores,
		name="beer_store_api"
	),

	# /stores/{store_id}
	url(
		regex=r"^stores/(?P<store_id>[0-9]+)/$",
		view=views.store_by_id,
		name="beer_store_api"
	),

	# /products
	url(
		regex=r"^products/$",
		view=views.products,
		name="beer_store_api"
	),

    # /beers
	url(
		regex=r"^beers/$",
		view=views.beers,
		name="beer_store_api"
	),

    # /beers/{product_id}
	url(
		regex=r"^beers/(?P<beer_id>[0-9]+)/$",
		view=views.beer_by_id,
		name="beer_store_api"
	),

    # /beers/{product_id}
	url(
		regex=r"^beers/(?P<beer_id>[0-9]+)/products/$",
		view=views.beer_products,
		name="beer_store_api"
	),

	# /products/{product_id}
	url(
		regex=r"^products/(?P<product_id>[0-9]+)/$",
		view=views.product_by_id,
		name="beer_store_api"
	),

	# /stores/{store_id}/products
	url(
		regex=r"^stores/(?P<store_id>[0-9]+)/products/$",
		view=views.products_at_store,
		name="beer_store_api"
	),

	# /products/{product_id}/stores
	url(
	    regex=r"^products/(?P<product_id>[0-9]+)/stores/$",
	    view=views.stores_with_product,
	    name="beer_store_api"
	),
)
