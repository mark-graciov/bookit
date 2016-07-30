from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tale_list, name='tale_list'),
    url(r'^tale-details/(?P<tale_id>[0-9]+)$', views.tale_details, name='tale_details'),
    url(r'^create-tale/(?P<tale_id>[0-9]+)$', views.create_tale, name='create_tale'),
    url(r'^download-tale/(?P<s_id>[a-z0-9]+)$', views.download_tale, name='download_tale'),
    url(r'^download-tale-doc/(?P<s_id>[a-z0-9]+)$', views.download_tale_doc, name='download_tale_doc'),
    url(r'^despre_noi', views.despre_noi, name='about'),
]
