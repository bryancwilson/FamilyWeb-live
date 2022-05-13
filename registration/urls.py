from django.urls import path
from . import views

# path function uses three mandatory arguments 1st being the section of the url that will be contained to map to that specific view
# , the 2nd being the actual view that the url maps to, and 3rd the name argument for easy reference of the urls.

# When ever the url is searched, the corresponding path function is called and the the view within that path function is called.
# at the end of every view there is code that will render a webpage either using or not using an html template

app_name = 'registration'
urlpatterns = [
    # ex: /registration/
    path('', views.index, name='index'),
    
]