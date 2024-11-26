from django.shortcuts import render
from django.http.response import HttpResponse

from book.models import book
# Create your views here.

def index(request):
    bb = book.objects.all()
    return render(request, 'index.html', locals())

def onebook(request, id):
    b = book.objects.get(id=id)
    return render(request, "onebook.html", locals())

