from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.paginator import Paginator

from qa.models import Question, Answer

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def index(request):
	page = request.GET.get('page',1)
	limit = request.GET.get('limit',10)
	questions = Question.objects.new()
	paginator = Paginator(questions, limit)
	page = paginator.page(page)
	return render(request,'templates/questions.html',{
	 'questions': page.object_list,
	 'paginator': paginator, 'page':page,
	})
	
	
