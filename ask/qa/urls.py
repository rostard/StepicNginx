from django.conf.urls import url

from .views import question

urlpatterns = [
	url(r'^(?P<num>\d+)/$',question),
]
