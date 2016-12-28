from django.conf.urls inmport url
from howdy import views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view())
]