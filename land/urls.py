from django.conf.urls import url
from land import views

urlpatterns = [
    url(
        regex=r"^$",
        view=views.index,
        name="landing_page"
    ),

    url(
        regex=r"^about/$",
        view=views.about,
        name="about_page"
    ),

    url(
        regex=r"^demos/$",
        view=views.demos,
        name="demos_page"
    ),
]
