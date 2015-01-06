from django.conf.urls import patterns, url

from keyterms import views

urlpatterns = patterns('',
    url(r'^$', views.index_keyterms, name = 'index_keyterms'),
    url(r'^new/(\d+)?$', views.new_keyterm, name = 'new_keyterm'),
    url(r'^edit/(\d+)$', views.edit_keyterm, name = 'edit_keyterm'),
    url(r'^delete/(\d+)$', views.delete_keyterm, name = 'delete_keyterm'),
    url(r'^change_status/(\d+)$', views.change_status, name = 'change_status'),
)
