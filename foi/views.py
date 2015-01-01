from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from ajax import *

from foi.models import Case
from foi.forms import CaseForm

@login_required
def index_case(request):
    cases = Case.objects.order_by('-created_date')
    return render(request, 'foi/index.html', {'cases': cases})

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
