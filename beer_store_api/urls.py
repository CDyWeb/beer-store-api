from django.conf.urls import url, include

urlpatterns = [
    url(r'', include('products.urls')),
    url(r'', include('land.urls')),
]
