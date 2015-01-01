from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from foxfoi.ajax import *

from mp.models import MP
from mp.forms import MPForm

@login_required
def index_mp(request):
    mps = MP.objects.order_by('name')
    return render(request, 'mp/index.html', {'indexitems': mps})

@login_required
def new_mp(request):
    if request.method == 'POST':
        form = MPForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            MP.objects.create_mp(cd['title'], cd['name'], cd['party'], cd['constituency'], cd['address'], cd['postcode'])
            return HttpResponseRedirect(reverse('mp:index_mp'))
    else:
        form = MPForm()
    return render(request, 'mp/new.html', {'form': form})

@login_required
def edit_mp(request, mp_id):
    mp = get_object_or_404(MP, pk = mp_id)
    if request.method == 'POST':
        form = MPForm(request.POST, instance = mp)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mp:index_mp'))
    else:
        form = MPForm(instance = mp)
    return render(request, 'mp/edit.html', {'mp': mp, 'form': form})

@login_required
def delete_mp(request, mp_id):
    mp = get_object_or_404(MP, pk = mp_id)
    if request.method == 'POST':
        mp.delete()
        return HttpResponseRedirect(reverse('mp:index_mp'))
    else:
        return render(request, 'mp/delete.html', {'mp': mp})
