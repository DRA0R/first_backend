from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request):
    lastest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "lastest_question_list": lastest_question_list
    })

def detail(request,question_id):
    #question = Question.objects.get(pk=question_id)  Si no se encuentra puede traer un error
    question = get_object_or_404(Question, pk=question_id)
    return render(request,"polls/detail.html", {
        "question" : question
    })

def results(request,question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta numero: {question_id}")

def vote(request,question_id):
    return HttpResponse(f"Estas votando a la pregunta numero: {question_id}")