from django.shortcuts import render

from post.models import Post
from django.http import HttpResponse

# Django teamplates
def posts_list(request):
    queryset = Post.objects.all()
    print(queryset)
    return render(request, 'listing.html',{'posts': queryset})


# ----------------------------------------------------------

# REST
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer

@api_view(['GET'])
def posts_list_api_view(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# first variant
def post_detail(request, id):

#     post = Post.objects.get(id=id)
#     serializer = PostSerializer(post)
#     return Response(serializer.data)

# second variant
    try:
        post = Post.objects.get(id = id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response('that object does not excist')









#     # queryset - позволяет читать  бд,фильтроват и изменять порядок
#
#     # objects - это Manager который позволяет нам работать с бд. они предоставляют нам доступ через методы
#     # к Djang ORM(которая отправляет запросы в бд).
#     # Это интерфейс который позволяет работать с бд через модели
#
#     # Model.objects.all()
#     # method all() - возвращает QuerySet всех обьектов в бд , то же самое что и SELECT * from table_name
#         Post.objects.all()[:5] можно мспользовать срезы
#
#     # Post.object.filter(created_at_year = 2022)
#     # Post.object.filter(category = 1)
#     # Post.objects.all().filter(category = 1)
#     # filter(**kwargs) - возвращает новый QuerySet ,содержащий обьекты
#     # ,который соответствует заданным параметрам поиска
#
#     # exclude(**kwargs)
#     # Post.object.exclude(category = 1)
#     # Возвращает QuerySet состоящий из элементов не соответствующих заланным параметрам
#
#     # get()
#     # Post.objects.get(id = 1) вернет запись с ip = 1
#     возвращает QuerySet который содержит лишь один обьект по условию

        # order_by()
        # Post.objects.order_by('-price') с минусом фильтрует по убыванию