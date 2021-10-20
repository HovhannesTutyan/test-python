from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def index(request):
    return render(request, 'app1/index.html');

def saveBook(request):
    # print(request.GET['name']);
    # print(request.GET['price']);
    # print(request.GET['pages']);
    name=request.GET['name'];
    price=request.GET['price'];
    # pages=request.GET['pages'];
    book = Book(name=name, price=price);
    try:
        book.save();
        return HttpResponse('true')
    except:
        return HttpResponse('false')
def getAllBooks(request):
    l = list();
    books = Book.objects.all();
    for bk in books:
        ser = BookSerializer(bk)
        l.append(ser.data)
    # print(l)
    import json;
    return HttpResponse(json.dumps(l));
def deleteBook(request):
    try:
        print(request.GET['id']);
        book = Book.objects.get(id=request.GET['id']);
        book.delete();
        return HttpResponse('true')
    except:
        return HttpResponse('false')




