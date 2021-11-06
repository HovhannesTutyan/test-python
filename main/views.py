from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import Post
from django.http import JsonResponse
# def home_view(request):
#     return render(request, "posts/main.html")

class MainView(TemplateView):
    template_name = 'posts/main.html'

class PostJsonListView(View):
    def get(self, *args, **kwargs):
        print(args, kwargs) # (<WSGIRequest: GET '/posts-json/3/'>,) {'num_posts': 3}
        upper = kwargs.get('num_posts') #3
        lower = upper - 3
        posts = list(Post.objects.values()[lower:upper]) #show posts from lower to upper boundaries
        posts_size = len(Post.objects.all())
        max_size = True if upper >= posts_size else False
        return JsonResponse({'data':posts, 'max':max_size}, safe=False)
