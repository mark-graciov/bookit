from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tale_list, name='tale_list'),
    url(r'^create-tale/$', views.create_tale, name='create_tale'),
    url(r'^create-tale/(?P<tale_id>[0-9]+)$', views.create_tale, name='create_tale'),
    url(r'^tale-details/(?P<tale_id>[0-9]+)$', views.tale_details, name='tale_details'),
]
