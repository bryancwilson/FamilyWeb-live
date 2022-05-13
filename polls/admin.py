from django.contrib import admin
from .models import Question # because the question object has an admin interface

# Register your models here.

admin.site.register(Question)