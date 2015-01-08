from django.conf.urls import patterns, url

from foi import views

urlpatterns = patterns('',
    url(r'^$', views.index_case, name = 'index_case'),
    url(r'^new/$', views.new_case, name = 'new_case'),
    url(r'^edit/(\d+)$', views.edit_case, name = 'edit_case'),
    url(r'^delete/(\d+)$', views.delete_case, name = 'delete_case'),
    url(r'^edit/(\d+)/comments$', views.case_comments, name = 'case_comments'),
    url(r'^edit/(\d+)/comments/(\d+)/edit$', views.edit_comment, name = 'edit_comment'),
    url(r'^edit/(\d+)/comments/(\d+)/delete$', views.delete_comment, name = 'delete_comment'),
    url(r'^edit/(\d+)/assessment$', views.case_assessment, name = 'case_assessment'),
    url(r'^edit/(\d+)/outcome$', views.case_outcome, name = 'case_outcome'),
    url(r'^edit/(\d+)/internal_review$', views.case_ir, name = 'case_internal_review'),
    url(r'^edit/(\d+)/information_commissioner_appeal$', views.case_ica, name = 'case_ica'),
    url(r'^edit/(\d+)/administrative_appeals_tribunal$', views.case_aat, name = 'case_aat'),
    # docgen
    url(r'^edit/(\d+)/generate_fee_doc$', views.generate_fee_doc, name = 'generate_fee_doc'),
    url(r'^edit/(\d+)/generate_notice_of_consultation_applicant$', views.generate_notice_of_consultation_applicant, name = 'generate_notice_of_consultation_applicant'),
    url(r'^edit/(\d+)/generate_notice_of_consultation_third_party$', views.generate_notice_of_consultation_third_party, name = 'generate_notice_of_consultation_third_party'),
)
