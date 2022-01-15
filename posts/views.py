from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
from django.core import serializers
from .forms import PostForm
from profiles.models import Profile

def post_list_and_create(request):
    # qs = Post.objects.all()
    form = PostForm(request.POST or None)
    if form.is_valid():
        author = Profile.objects.get(user=request.user)
        instance = form.save(commit=False)
        instance.author = author
        instance.save()
        return JsonResponse ({
            'title':instance.title,
            'body':instance.body,
            'author':instance.author.user.username,
            'id':instance.id
        })
    context = {
        # 'qs':qs,
        'form':form,
    }
    return render(request, 'posts/main.html', context)
def hello_world_view(request):
    return JsonResponse({'text':'hello world'})
def load_post_data_view(request, **kwargs):
    num_posts = kwargs.get('num_posts')
    visible = 3
    upper = num_posts
    lower = upper - visible
    size = Post.objects.all().count()
    qs = Post.objects.all()
    #  data = serializers.serialize('json', qs)
    #  return JsonResponse({'qs':qs})  Object of type QuerySet is not JSON serializable
    #  return JsonResponse({'data':data}) serialized data is also not a good solution
    data = []
    for obj in qs:
        item = {
            'id': obj.id,
            'title': obj.title,
            'body': obj.body,
            'liked': True if request.user in obj.liked.all() else False,
            'count': obj.like_count,
            'author': obj.author.user.username
        }
        data.append(item)
    return JsonResponse({'data': data[lower:upper], 'size':size}) # slice data from lower to upper

def like_unlike_post(request):
    pk = request.POST.get('pk')
    obj = Post.objects.get(pk=pk)
    if request.user in obj.liked.all(): # if the user is in the list of liked post
        liked = False
        obj.liked.remove(request.user)
    else:
        liked = True
        obj.liked.add(request.user)
    return JsonResponse({'liked': liked, 'count': obj.like_count})

def post_detail(request, pk):
    object = Post.objects.get(pk=pk)
    form = PostForm()
    context = {
        'object': object,
        'form': form,
    }
    return render(request,'posts/detail.html', context)

def post_detail_data_view(request, pk):
    obj = Post.objects.get(pk=pk)
    data = {
        'id':obj.id,
        'title':obj.title,
        'body': obj.body,
        'author': obj.author.user.username,
        'logged_in': request.user.username
    }
    return JsonResponse({'data':data})

def update_post(request, pk):
    obj = Post.objects.get(pk=pk)
    new_title = request.POST.get('title')
    new_body = request.POST.get('body')
    obj.title = new_title
    obj.body = new_body
    obj.save()
    return JsonResponse({ 'title': new_title, 'body': new_body})

def delete_post(request, pk):
    obj = Post.objects.get(pk=pk)
    obj.delete()
    return JsonResponse({})