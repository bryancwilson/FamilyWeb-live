from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'contact/index.html')