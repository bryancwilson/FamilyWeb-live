from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'feedback/index.html') #when this function is called form the urls page, this page is rendered using the index.html template
