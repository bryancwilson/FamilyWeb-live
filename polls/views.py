from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.urls import reverse

# Create your views here.

# Django sees each website page to serve a certain purpose, and therefore can be boiled down to a function (def). each one of these functions
# are included in the views python file. 

# The render() function takes the request object as its 
# first argument, a template name as its second argument
# and a dictionary as its optional third argument. 
# It returns an HttpResponse object of the given template 
# rendered with the given context. The context is usually used as a dictionary
# that can be used in the html file for conditional operations.

# The shortcut get_object_or_404() raises the Http404 exception 
# if a question with the requested ID doesn’t exist.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', context) #when this function is called form the urls page, this page is rendered using the index.html template

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # if the object does not exist, then the 404 error will pop up.

    return render(request, 'polls/detail.html', {'question': question}) # when this function is called from the urls page, this details page is rendered using the detail.html template

# NOTICE THAT THIS FUNCTION IS INVOKED BUT THE DETAIL.HTML PAGE IS STILL VISIBLE UNTIL THE RETURN RESPONSE FUNCTION IS INVOKED
def vote(request, question_id): 
    question = get_object_or_404(Question, pk=question_id) #the question will be pulled if the question id that is inputted into the url exists, if not a 404 error will pop up
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist): #if the the user does not choose anything or chooses a choice that is not available the exception code is executed
        # Redisplay the question voting form.

        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1 #this increments the votes of the selected choice
        selected_choice.save()  # this saves the selected vote to the database table
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) # this function takes an argument for where the user should be redirected to after the functionality of one page if complete

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/results.html', {'question': question})