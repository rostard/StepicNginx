from django.core.paginator import Paginator
from django.shortcuts import render
from datetime import datetime, timedelta
import random
import string

from qa.models import Session, User


def paging(request, qr, url=""):
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)

    paginator = Paginator(qr, limit)
    paginator.baseurl = url + "/?page="
    page = paginator.page(page)
    return render(request, 'questions.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })


def do_login(login, password):
    try:
        user = User.objects.get(username=login)
    except User.DoesNotExist:
        return None
    hashed_pass = password #hash(password + "pile_of_salt")
    if not user.password == hashed_pass:
        return None
    session = Session()
    session.user = user
    session.key = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(100))
    session.expires = datetime.now() + timedelta(days=5)
    session.save()
    return session.key
