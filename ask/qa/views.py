from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator

from qa.models import Question, Answer
 
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def paging(request,qr):
	page = request.GET.get('page',1)
	limit = request.GET.get('limit',10)
	
	paginator = Paginator(qr, limit)
	paginator.baseurl = "/?page="
	page = paginator.page(page)
	return render(request,'questions.html',{
	 'questions': page.object_list,
	 'paginator': paginator, 'page': page,
	})

def index(request):
	qr = Question.objects.new()
	return paging(request,qr)

def popular(request):
	qr = Question.objects.popular()
	return paging(request,qr)
	
def new(request):
	qr = Question.objects.new()
	return paging(request,qr)

def question(request, num):
	try:
		q=Question.objects.get(id=num)
	except Question.DoesNotExist:
		raise Http404
	return render(request,'question.html',{
		'question' : q
	})
	

