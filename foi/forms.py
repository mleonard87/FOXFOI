from django import forms
from foi.models import Case, Comment, Assessment, Outcome, InternalReview, InformationCommissionerAppeal, AdministrativeAppealsTribunal

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'title', 
            'subject', 
            'received_date', 
            'enquiry_date', 
            'enquiry_ref', 
            'enquiry_method', 
            'response_method', 
            'enquiry_description', 
            'urgent_flag', 
            'handling_instructions',
            'addressee_name']
        labels = {
            'urgent_flag': ('Urgent?')
        }
        widgets = {
            'title': forms.TextInput(attrs = {'placeholder': 'Enter a title for this case'}),
            'received_date': forms.DateInput(attrs = {'type': 'date'}),
            'enquiry_date': forms.DateInput(attrs = {'type': 'date'}),
            'urgent_flag': forms.CheckboxInput(attrs = {'label': 'Urgent?'})
        }

class CaseEnquirerForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'enquirer_title',
            'enquirer_name',
            'enquirer_department',
            'enquirer_organisation',
            'enquirer_address',
            'enquirer_postcode',
            'enquirer_telephone',
            'enquirer_email_address',
            'enquirer_enquirer_group',
            'enquirer_industry_body',
            'enquirer_region']
        labels = {
            'enquirer_title': ('Title'),
            'enquirer_name': ('Name'),
            'enquirer_department': ('Department'),
            'enquirer_organisation': ('Organisation'),
            'enquirer_address': ('Address'),
            'enquirer_postcode': ('Postcode'),
            'enquirer_telephone': ('Telephone'),
            'enquirer_email_address': ('Email Address'),
            'enquirer_enquirer_group': ('Enquirer Group'),
            'enquirer_industry_body': ('Industry Body'),
            'enquirer_region': ('Region')
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'body']
        widgets = {
            'subject': forms.TextInput(attrs = {'placeholder': 'Enter a subject for this comment'}),
            'body': forms.Textarea(attrs = {'placeholder': 'Enter a body for this comment'})
        }

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = [
            'third_party_consultation',
            'precedents',
            'precedent_details']
        labels = {
            'third_party_consultation': ('Third Party Consultation Required?'),
            'precedents': ('Precedents Exist?')
        }
        widgets = {}
        help_texts = {}

class AssessmentFeeForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = [
            'fee_flag',
            'search_and_retrieval_time',
            'decision_making_time',
            'photocopy_charges',
            'other_access_time',
            'postage_charges',
            'initial_deposit',
            'request_general_description',
            'include_refine_request_flag',
            'include_third_party_consultation_flag',
            'request_concerning',
            'contact_name',
            'contact_telephone',

            'fee_notice_issued_flag',
            'fee_notice_issued_date',
            'fee_payment_required_date',
            'fee_paid_flag',
            'fee_received_date',
            'fee_limit_flag']
        labels = {
            'fee_flag': ('Fees Applicable?'),
            'include_refine_request_flag': ('Include Refine Request Clause?'),
            'include_third_party_consultation_flag': ('Include Third Party Consultation Clause?'),
            'fee_notice_issued_flag': ('Fee Notice Issued?'),
            'fee_paid_flag': ('Fee Paid?'),
            'fee_limit_flag': ('Fee Exceeds Cost Limit?')
        }
        widgets = {
            'fee_notice_issued_date': forms.DateInput(attrs = {'type': 'date'}),
            'fee_payment_required_date': forms.DateInput(attrs = {'type': 'date'}),
            'fee_received_date': forms.DateInput(attrs = {'type': 'date'})
        }

class AssessmentThirdPartyForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = [
            'third_party_request_general_description',
            'documents_attached_or_described',
            'include_s47_flag',
            'include_s47b_flag',
            'include_s47f_flag',
            'include_s47g_flag',
            'respond_by_date',
            'third_party_contact_name',
            'third_party_contact_telephone',

            'third_party_title',
            'third_party_name',
            'third_party_department',
            'third_party_organisation',
            'third_party_address',
            'third_party_postcode']
        labels = {
            'include_s47_flag': ('Include s47?'),
            'include_s47b_flag': ('Include s47B?'),
            'include_s47f_flag': ('Include s47F?'),
            'include_s47g_flag': ('Include s47G?')
        }
        widgets = {
            'respond_by_date': forms.DateInput(attrs = {'type': 'date'})
        }
        help_texts = {}

class OutcomeForm(forms.ModelForm):
    class Meta:
        model = Outcome
        fields = ['foi_outcomes', 'foi_exemptions', 'foi_conditional_exemptions', 'disclosure_outcomes', 'certificates']

class InternalReviewForm(forms.ModelForm):
    class Meta:
        model = InternalReview
        fields = ['requested_date', 'review_held_date', 'days_taken_to_hold_review', 'review_members', 'review_decision']
        widgets = {
            'requested_date': forms.DateInput(attrs = {'type': 'date'}),
            'review_held_date': forms.DateInput(attrs = {'type': 'date'})
        }

class InformationCommissionerAppealForm(forms.ModelForm):
    class Meta:
        model = InformationCommissionerAppeal
        fields = ['contacted_date', 'documents_provided_date', 'decision_recieved_date', 'decision', 'decision_notice']
        widgets = {
            'contacted_date': forms.DateInput(attrs = {'type': 'date'}),
            'documents_provided_date': forms.DateInput(attrs = {'type': 'date'}),
            'decision_recieved_date': forms.DateInput(attrs = {'type': 'date'})
        }

class AdministrativeAppealsTribunalForm(forms.ModelForm):
    class Meta:
        model = AdministrativeAppealsTribunal
        fields = ['contacted_date', 'documents_provided_date', 'decision_recieved_date', 'decision', 'decision_notice']
        widgets = {
            'contacted_date': forms.DateInput(attrs = {'type': 'date'}),
            'documents_provided_date': forms.DateInput(attrs = {'type': 'date'}),
            'decision_recieved_date': forms.DateInput(attrs = {'type': 'date'})
        }
