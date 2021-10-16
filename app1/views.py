from django.http import HttpResponse
from django.shortcuts import render

from .models import Book


def index(request):
    return render(request, 'app1/index.html');

def saveBook(request):
    # print(request.GET['name']);
    # print(request.GET['price']);
    # print(request.GET['pages']);
    name=request.GET['name'];
    price=request.GET['price'];
    pgs=request.GET['pages'];
    book = Book(name=name, price=price, pages=pgs);
    try:
        book.save();
        return HttpResponse('true')
    except:
        return HttpResponse('false')
