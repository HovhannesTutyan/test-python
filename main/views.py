from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Post

class BaseView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        posts = Post.objects.all()[:2]
        return render(request, 'base.html', {'posts':posts})

class DynamicPostsLoad(View):
    @staticmethod
    def get(request, *args, **kwargs):
        last_post_id = request.GET.get('lastPostId')
        more_posts = Post.objects.filter(pk__gt=int(last_post_id)).values('id', 'title')[:2]
        if not more_posts:
            return JsonResponse({'data':False})
        data = []
        for post in more_posts:
            obj = {
                'id':post['id'],
                'title':post['title'],
                'last_post':last_post_id
            }
            data.append(obj)
            data[-1]['last_post']=True
        return JsonResponse({'data':data})