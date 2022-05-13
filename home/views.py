from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from django.urls import reverse

# Create your views here.

def index(request):
    context = 'This is the home page'
    return render(request, 'home/index.html', {'context': context})