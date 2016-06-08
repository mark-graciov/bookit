from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.tale_list, name='tale_list'),
	url(r'^create-tale/(?P<tale_id>[0-9]+)$', views.create_tale, name='create_tale'),
]
