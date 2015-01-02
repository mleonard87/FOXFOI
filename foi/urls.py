from django.conf.urls import patterns, url

from foi import views

urlpatterns = patterns('',
    url(r'^$', views.index_case, name = 'index_case'),
    url(r'^new/$', views.new_case, name = 'new_case'),
    url(r'^edit/(\d+)$', views.edit_case, name = 'edit_case'),
    url(r'^edit/(\d+)/comments$', views.case_comments, name = 'case_comments'),
    url(r'^edit/(\d+)/comments/(\d+)/edit$', views.edit_comment, name = 'edit_comment'),
    url(r'^edit/(\d+)/comments/(\d+)/delete$', views.delete_comment, name = 'delete_comment'),
    url(r'^delete/(\d+)$', views.delete_case, name = 'delete_case'),
)
