from django.db import models
from django.utils import timezone

import datetime

# Create your models here.

# CharField (character field) and DateTimeField (datetimes) are types of fields that were made by the django.db.models.Model class.
# the database will create columns out of these parameters using the names I set them equal too, question_text and pub_date
# Question (the class name) is the name of the table
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):          # important to add this section to the code to return the list of objects in the API
        return self.question_text

    def was_published_recently(self): #when function is called, it will return true if the question was published recently
        return self.pub_date >= timezone.now()
datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE) #That tells Django each Choice is related to a single Question. Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)

    def __str__(self):  
        return self.choice_text