from django.core.paginator import Paginator
from django.shortcuts import render
from datetime import  timedelta
from django.utils import timezone
import random
import string

from qa.models import Session, User


def cook_auth(request):
    sessionid = request.COOKIES.get('sessionid', None)
    if sessionid:
        session = Session.objects.get(key=sessionid)
        if session.expires > timezone.now():
            return session.user

    return None


def paging(request, qr, url=""):
    user = cook_auth(request)
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)

    paginator = Paginator(qr, limit)
    paginator.baseurl = url + "/?page="
    page = paginator.page(page)
    return render(request, 'questions.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
        'user': user
    })


def do_login(login, password):
    try:
        user = User.objects.get(username=login)
    except User.DoesNotExist:
        return None
    hashed_pass = hash(password + "pile_of_salt")
    if not user.password == str(hashed_pass):
        return hashed_pass
    session = Session()
    session.user = user
    session.key = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(100))
    session.expires = timezone.now() + timedelta(days=5)
    session.save()
    return session.key
