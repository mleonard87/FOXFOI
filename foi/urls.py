from django.conf.urls import patterns, url

from foi import views

urlpatterns = patterns('',
    url(r'^$', views.index_case, name = 'index_case'),
    url(r'^new/$', views.new_case, name = 'new_case'),
    url(r'^edit/(\d+)$', views.edit_case, name = 'edit_case'),
    url(r'^delete/(\d+)$', views.delete_case, name = 'delete_case'),
)
