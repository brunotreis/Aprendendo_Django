from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Question
from django.template import loader





# Leave the rest of the views (detail, results, vote) unchanged

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

#def index(request):
#    return HttpResponse('Universidade Federal do Oeste da Bahia')

def detail(request, question_id):
    return HttpResponse('Você está olhando a questão %s.' %question_id)

def results(request, question_id):
    response = 'Você está olhando o resultado da questão %s.'
    return HttpResponse( response % question_id)

def vote(request, question_id):
    return HttpResponse('Você está votando na questão %s.' %question_id)