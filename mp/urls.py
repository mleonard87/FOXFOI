from django.conf.urls import patterns, url

from mp import views

urlpatterns = patterns('',
    url(r'^$', views.index_mp, name = 'index_mp'),
    url(r'^new/$', views.new_mp, name = 'new_mp'),
    url(r'^edit/(\d+)$', views.edit_mp, name = 'edit_mp'),
    url(r'^delete/(\d+)$', views.delete_mp, name = 'delete_mp'),
)
