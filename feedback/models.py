from django.db import models
from django.utils import timezone

import datetime


# Create your models here.

class Review(models.Model):
    review_text = models.CharField(max_length = 500)
    user_FirstName = models.CharField(max_length = 100)
    user_LastName = models.CharField(max_length = 100)

    def __str__(self):          # important to add this section to the code to return the list of objects in the API
        return self.review_text