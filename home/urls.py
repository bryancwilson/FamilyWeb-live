from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    # ex: /feedback/
    path('', views.index, name='index'),
    
    
]