from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from ajax import *

@login_required
def index(request):
    return render(request, 'foi/index.html')
