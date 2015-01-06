from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from foxfoi.ajax import *

from keyterms.models import KeyTerm
from keyterms.forms import KeyTermForm

@login_required
def index_keyterms(request):
    keyterms = KeyTerm.objects.get_parent_key_terms();
    return render(request, 'keyterms/index.html', {'indexitems': keyterms})

@login_required
def new_keyterm(request, parent_id):
    parent_kt = None
    if parent_id != None:
        parent_kt = get_object_or_404(KeyTerm, pk = parent_id)
    if request.method == 'POST':
        form = KeyTermForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            KeyTerm.objects.create_key_term(cd['name'], parent_kt)
            return HttpResponseRedirect(reverse('keyterms:index_keyterms'))
    else:
        form = KeyTermForm()
    return render(request, 'keyterms/new.html', {'form': form, 'parent_kt': parent_kt})

@login_required
def edit_keyterm(request, kt_id):
    keyterm = get_object_or_404(KeyTerm, pk = kt_id)
    if request.method == 'POST':
        form = KeyTermForm(request.POST, instance = keyterm)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('keyterms:index_keyterms'))
    else:
        form = KeyTermForm(instance = keyterm)
    return render(request, 'keyterms/edit.html', {'keyterm': keyterm, 'form': form})

@login_required
def change_status(request, kt_id):
    keyterm = get_object_or_404(KeyTerm, pk = kt_id)
    keyterms = KeyTerm.objects.get_parent_key_terms();
    if request.method == 'POST':
        keyterm.change_status()
        return HttpResponseRedirect(reverse('keyterms:index_keyterms'))
    return render(request, 'keyterms/index.html', {'indexitems': keyterms})

@login_required
def delete_keyterm(request, kt_id):
    keyterm = get_object_or_404(KeyTerm, pk = kt_id)
    if request.method == 'POST':
        keyterm.delete()
        return HttpResponseRedirect(reverse('keyterms:index_keyterms'))
    else:
        return render(request, 'keyterms/delete.html', {'keyterm': keyterm})
