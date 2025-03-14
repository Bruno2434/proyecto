from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse('Estas viendo la pregunta %s' % question_id)

def results(request, question_id):
    response = 'Estas viendo la respuesta para la pregunta %s'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('Estas viendo las votaciones para la pregunta %s' % question_id)
