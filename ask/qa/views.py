from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect

from qa.forms import AskForm, AnswerForm, SignUpForm, LoginForm
from qa.models import Question, Answer, User, Session
from qa.shortcuts import paging, do_login
from datetime import datetime, timedelta


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request):
    qr = Question.objects.new()
    return paging(request, qr)


def popular(request):
    qr = Question.objects.popular()
    return paging(request, qr, "/popular")


def new(request):
    qr = Question.objects.new()
    return paging(request, qr, "/new")


def ask(request):
    sessionid = request.COOKIES.get('sessionid', None)
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            q = form.save()
            if sessionid:
                session = Session.objects.get(key=sessionid)
                author = session.user
                q.author = author
                q.save()
            return HttpResponseRedirect(q.get_url())
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form': form,
    })


def question(request, num):
    sessionid = request.COOKIES.get('sessionid', None)
    try:
        q = Question.objects.get(id=num)
    except Question.DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            if sessionid:
                session = Session.objects.get(key=sessionid)
                author = session.user
                answer.author = author
                answer.save()
            return HttpResponseRedirect(q.get_url())

    form = AnswerForm(initial={'question': q.id})
    answers = Answer.objects.filter(question=q)

    return render(request, 'question.html', {
        'question': q,
        'answers': answers,
        'form': form,
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        url = request.POST.get('continue', '/')
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password')
            sessionid = do_login(username, password)
            response = HttpResponseRedirect(url)
            response.set_cookie('sessionid', sessionid, httponly=True, expires=datetime.now() + timedelta(days=5))
            return response
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {
            'form': form,
        })


def login(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        url = request.POST.get('continue', '/')
        sessionid = do_login(username, password)
        if sessionid:
            response = HttpResponseRedirect(url)
            response.set_cookie('sessionid', sessionid, httponly=True, expires=datetime.now() + timedelta(days=5))
            return response
        else:
            error = u'Неверный логин или пароль'
    form = LoginForm()
    return render(request, 'login.html', {
        'form': form,
        'error': error,
    })
