from django.urls import path
from . import views

app_name = 'agenda'
urlpatterns = [
    # ex: /agenda/
    path('', views.index, name='index'),
    
    
]