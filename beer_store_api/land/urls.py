from django.conf.urls import patterns, url
from land import views

urlpatterns = patterns("",
	url(
		regex=r"^$",
		view=views.index,
		name="landing_page"
	),

	url(
		regex=r"^about/$",
		view=views.about,
		name="landing_page"
	),

	url(
		regex=r"^demos/$",
		view=views.demos,
		name="landing_page"
	),
)
