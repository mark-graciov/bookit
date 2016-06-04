from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.tale_list, name='tale_list'),
	url(r'^create-book/(?P<tale_id>[0-9]+)$', views.create_book, name='create_book'),
]
