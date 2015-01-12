from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from foxfoi.ajax import *

from mps.models import MP
from mps.forms import MPForm

@login_required
def index_mp(request):
    searchTerm = request.GET.get('searchTerm')
    searchTermDisplay = searchTerm if searchTerm != None else ""

    mp_list = MP.objects.search_mps(searchTerm)
    paginator = Paginator(mp_list, settings.PAGINATION_PAGES)

    queries = request.GET.copy()
    if queries.has_key('page'):
        del queries['page']

    page = request.GET.get('page')
    try:
        mps = paginator.page(page)
    except PageNotAnInteger:
        mps = paginator.page(1)
    except EmptyPage:
        mps = paginator.page(paginator.num_pages)
    return render(request, 'mps/index.html', {'indexitems': mps, 'searchTerm': searchTermDisplay, 'queries': queries})

@login_required
def new_mp(request):
    if request.method == 'POST':
        form = MPForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            MP.objects.create_mp(cd['title'], cd['name'], cd['party'], cd['constituency'], cd['address'], cd['postcode'])
            return HttpResponseRedirect(reverse('mps:index_mp'))
    else:
        form = MPForm()
    return render(request, 'mps/new.html', {'form': form})

@login_required
def edit_mp(request, mp_id):
    mp = get_object_or_404(MP, pk = mp_id)
    if request.method == 'POST':
        form = MPForm(request.POST, instance = mp)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mps:index_mp'))
    else:
        form = MPForm(instance = mp)
    return render(request, 'mps/edit.html', {'mp': mp, 'form': form})

@login_required
def delete_mp(request, mp_id):
    mp = get_object_or_404(MP, pk = mp_id)
    if request.method == 'POST':
        mp.delete()
        return HttpResponseRedirect(reverse('mps:index_mp'))
    else:
        return render(request, 'mps/delete.html', {'mp': mp})
