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
    url(r'^edit/(\d+)/referrals$', views.case_referrals, name = 'case_referrals'),
    url(r'^edit/(\d+)/referrals/(\d+)/edit$', views.edit_referral, name = 'edit_referral'),
    url(r'^edit/(\d+)/referrals/(\d+)/delete$', views.delete_referral, name = 'delete_referral'),
    url(r'^edit/(\d+)/referrals/(\d+)/complete$', views.complete_referral, name = 'complete_referral'),
    url(r'^edit/(\d+)/assessment$', views.case_assessment, name = 'case_assessment'),
    url(r'^edit/(\d+)/outcome$', views.case_outcome, name = 'case_outcome'),
    url(r'^edit/(\d+)/internal_review$', views.case_ir, name = 'case_internal_review'),
    url(r'^edit/(\d+)/information_commissioner_appeal$', views.case_ica, name = 'case_ica'),
    url(r'^edit/(\d+)/administrative_appeals_tribunal$', views.case_aat, name = 'case_aat'),
    # docgen
    url(r'^edit/(\d+)/preview_fee_doc$', views.preview_fee_doc, name = 'preview_fee_doc'),
    url(r'^edit/(\d+)/download_fee_doc$', views.download_fee_doc, name = 'download_fee_doc'),
    url(r'^edit/(\d+)/preview_notice_of_consultation_applicant$', views.preview_notice_of_consultation_applicant, name = 'preview_notice_of_consultation_applicant'),
    url(r'^edit/(\d+)/download_notice_of_consultation_applicant$', views.download_notice_of_consultation_applicant, name = 'download_notice_of_consultation_applicant'),
    url(r'^edit/(\d+)/preview_notice_of_consultation_third_party$', views.preview_notice_of_consultation_third_party, name = 'preview_notice_of_consultation_third_party'),
    url(r'^edit/(\d+)/download_notice_of_consultation_third_party$', views.download_notice_of_consultation_third_party, name = 'download_notice_of_consultation_third_party'),
)
