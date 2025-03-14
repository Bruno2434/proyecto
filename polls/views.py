from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('hola mundo')

def detail(request, question_id):
    return HttpResponse('Estas viendo la pregunta %s' % question_id)

def results(request, question_id):
    response = 'Estas viendo la respuesta para la pregunta %s'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('Estas viendo las votaciones para la pregunta %s' % question_id)
