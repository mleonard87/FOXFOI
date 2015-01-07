from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from foxfoi.ajax import *

from foi.models import Case, Comment, Assessment, Outcome, InternalReview, InformationCommissionerAppeal, AdministrativeAppealsTribunal
from foi.forms import CaseForm, CommentForm, AssessmentForm, AssessmentFeeForm, AssessmentThirdPartyForm, OutcomeForm, InternalReviewForm, InformationCommissionerAppealForm, AdministrativeAppealsTribunalForm

@login_required
def index_case(request):
    cases = Case.objects.order_by('-created_date')
    return render(request, 'foi/index.html', {'indexitems': cases})

@login_required
def new_case(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Case.objects.create_case(cd['title'], request.user)
            return HttpResponseRedirect(reverse('foi:index_case'))
    else:
        form = CaseForm()
    return render(request, 'foi/new.html', {'form': form})

@login_required
def edit_case(request, case_id):
    case = get_object_or_404(Case, pk = case_id)
    if request.method == 'POST':
        form = CaseForm(request.POST, instance = case)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('foi:edit_case', args = (case_id,)))
    else:
        form = CaseForm(instance = case)
    return render(request, 'foi/edit.html', {'case': case, 'form': form})

@login_required
def delete_case(request, case_id):
    case = get_object_or_404(Case, pk = case_id)
    if request.method == 'POST':
        case.delete()
        return HttpResponseRedirect(reverse('foi:index_case'))
    else:
        return render(request, 'foi/delete.html', {'case': case})

@login_required
def case_comments(request, case_id):
    case = get_object_or_404(Case, pk = case_id)
    comments = Comment.objects.filter(case = case).order_by('-created_date')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Comment.objects.create_comment(case, cd['subject'], cd['body'], request.user)
            return HttpResponseRedirect(reverse('foi:case_comments', args = (case_id,)))
    else:
        form = CommentForm()
    return render(request, 'foi/comments.html', {'case': case, 'indexitems': comments, 'form': form})

@login_required
def edit_comment(request, case_id, comment_id):
    case = get_object_or_404(Case, pk = case_id)
    comment = get_object_or_404(Comment, pk = comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance = comment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('foi:case_comments', args = (case_id,)))
    else:
        form = CommentForm(instance = comment)
    return render(request, 'foi/edit_comment.html', {'case': case, 'comment': comment, 'form': form})

@login_required
def delete_comment(request, case_id, comment_id):
    case = get_object_or_404(Case, pk = case_id)
    comment = get_object_or_404(Comment, pk = comment_id)
    if request.method == 'POST':
        comment.delete()
        return HttpResponseRedirect(reverse('foi:case_comments', args = (case_id,)))
    else:
        return render(request, 'foi/delete_comment.html', {'case': case, 'comment': comment})

@login_required
def case_assessment(request, case_id):
    case = get_object_or_404(Case, pk = case_id)
    if request.method == 'POST':
        assessment = get_object_or_404(Assessment, case = case_id)
        assessment_form = AssessmentForm(request.POST, instance = assessment)
        assessment_fee_form = AssessmentFeeForm(request.POST, instance = assessment)
        assessment_third_party_form = AssessmentThirdPartyForm(request.POST, instance = assessment)
        if assessment_form.is_valid() and assessment_fee_form.is_valid() and assessment_third_party_form.is_valid():
            assessment_form.save()
            assessment_fee_form.save()
            assessment_third_party_form.save()
            return HttpResponseRedirect(reverse('foi:case_assessment', args = (case_id,)))
    else:
        try:
            assessment = Assessment.objects.get(case = case_id)
        except ObjectDoesNotExist:
            assessment = Assessment.objects.create_assessment(case)
        assessment_form = AssessmentForm(instance = assessment)
        assessment_fee_form = AssessmentFeeForm(instance = assessment)
        assessment_third_party_form = AssessmentThirdPartyForm(instance = assessment)
    return render(request, 'foi/assessment.html', {'case': case, 'assessment_form': assessment_form, 'assessment_fee_form': assessment_fee_form, 'assessment_third_party_form': assessment_third_party_form})

@login_required
def case_outcome(request, case_id):
    case = get_object_or_404(Case, pk = case_id)
    if request.method == 'POST':
        outcome = get_object_or_404(Outcome, case = case_id)
        form = OutcomeForm(request.POST, instance = outcome)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('foi:case_outcome', args = (case_id,)))
    else:
        try:
            outcome = Outcome.objects.get(case = case_id)
        except ObjectDoesNotExist:
            outcome = Outcome.objects.create_outcome(case)
        form = OutcomeForm(instance = outcome)
    return render(request, 'foi/outcome.html', {'case': case, 'form': form})

@login_required
def case_ir(request, case_id):
    case = get_object_or_404(Case, pk = case_id)
    if request.method == 'POST':
        ir = get_object_or_404(InternalReview, case = case_id)
        form = InternalReviewForm(request.POST, instance = ir)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('foi:case_internal_review', args = (case_id,)))
    else:
        try:
            ir = InternalReview.objects.get(case = case_id)
        except ObjectDoesNotExist:
            ir = InternalReview.objects.create_internal_review(case)
        form = InternalReviewForm(instance = ir)
    return render(request, 'foi/ir.html', {'case': case, 'form': form})

@login_required
def case_ica(request, case_id):
    case = get_object_or_404(Case, pk = case_id)
    if request.method == 'POST':
        ica = get_object_or_404(InformationCommissionerAppeal, case = case_id)
        form = InformationCommissionerAppealForm(request.POST, instance = ica)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('foi:case_ica', args = (case_id,)))
    else:
        try:
            ica = InformationCommissionerAppeal.objects.get(case = case_id)
        except ObjectDoesNotExist:
            ica = InformationCommissionerAppeal.objects.create_information_commissioner_appeal(case)
        form = InformationCommissionerAppealForm(instance = ica)
    return render(request, 'foi/ica.html', {'case': case, 'form': form})

@login_required
def case_aat(request, case_id):
    case = get_object_or_404(Case, pk = case_id)
    if request.method == 'POST':
        aat = get_object_or_404(AdministrativeAppealsTribunal, case = case_id)
        form = AdministrativeAppealsTribunalForm(request.POST, instance = aat)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('foi:case_aat', args = (case_id,)))
    else:
        try:
            aat = AdministrativeAppealsTribunal.objects.get(case = case_id)
        except ObjectDoesNotExist:
            aat = AdministrativeAppealsTribunal.objects.create_administrative_appeals_tribunal(case)
        form = AdministrativeAppealsTribunalForm(instance = aat)
    return render(request, 'foi/aat.html', {'case': case, 'form': form})
