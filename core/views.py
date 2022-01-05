from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .model_serializer import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# @csrf_exempt
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all() # articles become a queryset
        serializer = ArticleSerializer(articles, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=201) #created status
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    try:
        article=Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


