from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = "polls/index.html"
    context = {"latest_question_list": latest_question_list}
    return render(request, template, context)


def detail(request, question_id):
    template = "polls/detail.html"
    q = get_object_or_404(Question, pk=question_id)
    context = {"question": q}
    return render(request, template, context)

def results(request, question_id):
    return HttpResponse("You are looking at the RESULT of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
