from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator

from qa.forms import AskForm, AnswerForm
from qa.models import Question, Answer


def test(request, *args, **kwargs):
	return HttpResponse('OK')


def paging(request, qr, url=""):
	page = request.GET.get('page',1)
	limit = request.GET.get('limit',10)
	
	paginator = Paginator(qr, limit)
	paginator.baseurl = url+"/?page="
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
	return paging(request,qr,"/popular")


def new(request):
	qr = Question.objects.new()
	return paging(request,qr,"/new")


def ask(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		if form.is_valid():
			question = form.save()
			return HttpResponseRedirect(question.get_url())
	else:
		form = AskForm()
	return render(request, 'ask.html', {
		'form': form,
	})


def question(request, num):
	try:
		q=Question.objects.get(id=num)
	except Question.DoesNotExist:
		raise Http404

	if request.method == "POST":
		form = AnswerForm(request.POST)
		if form.is_valid():
			answer = form.save()
			return HttpResponseRedirect(q.get_url())

	form = AnswerForm(initial={'question': q.id})
	answers = Answer.objects.filter(question=q)

	return render(request,'question.html', {
		'question': q,
		'answers': answers,
		'form': form,
	})
	

