from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from foxfoi.ajax import *

from foi.models import Case, Comment
from foi.forms import CaseForm, CommentForm

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
            return HttpResponseRedirect(reverse('foi:index_case'))
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
def case_outcome(request, case_id):
    case = get_object_or_404(Case, pk = case_id)
    return render(request, 'foi/outcome.html', {'case': case})

@login_required
def case_ir(request, case_id):
    case = get_object_or_404(Case, pk = case_id)
    return render(request, 'foi/ir.html', {'case': case})

@login_required
def case_ica(request, case_id):
    case = get_object_or_404(Case, pk = case_id)
    return render(request, 'foi/ica.html', {'case': case})

@login_required
def case_aat(request, case_id):
    case = get_object_or_404(Case, pk = case_id)
    return render(request, 'foi/aat.html', {'case': case})
