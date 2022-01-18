from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import JsonResponse

def store(request):
    if request.method == "POST":
        obj = Customer()
        obj.name = request.POST.get('name')
        obj.email = request.POST.get('email')
        if len(request.FILES) != 0:
            obj.profile_pic = request.FILES['image']
        obj.save()
        return redirect('/checkout')
    return render(request, 'core/store.html')

def store_get_data(request, **kwargs):
    num_posts = kwargs.get('num_posts')
    visible = 3
    upper = num_posts
    lower = upper - visible
    size = Customer.objects.all().count()
    qs = Customer.objects.all()

    data = []
    for obj in qs:
        item = {
            'id': obj.id,
            'name': obj.name,
            'email': obj.email,
        }
        data.append(item)
    return JsonResponse({'data': data[lower:upper], 'size': size})

def detail_view(request, pk):
    obj = Customer.objects.get(pk=pk)
    data = {
        'id': obj.id,
        'name': obj.name,
        'email': obj.email,
        'image': obj.profile_pic
    }
    return render(request, 'core/checkout.html', data)