from django.conf.urls import url
from land import views

urlpatterns = [
    url(
        regex=r"^$",
        view=views.index,
        name="landing_page"
    ),
]
