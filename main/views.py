from django.shortcuts import render
from .models import Article
from django.http import JsonResponse

def HomeView(request):
    context = {
        'name':'test name',
        'address':'test address',
        'allarticles':Article.objects.all()
    }
    return render(request, "main.html", context)

def AboutView(request):
    context = {
        'about' : 'test django developer'
    }
    return render(request, "about.html", context)
def AllArticleView(request):
    context = {
        'allarticles': Article.objects.all()
    }
    return render(request, "allarticles.html", context)
def CreateArticteView(request):
    t = request.POST.get('title') #title=request.POST["title"]
    d = request.POST.get('description')
    try:
        Article.objects.create(title=t, description=d)
        resp={
            'status':'success',
        }
    except Exception as e:
        print(e)
        resp = {
            'status': 'fault',
        }
    return JsonResponse(resp)
