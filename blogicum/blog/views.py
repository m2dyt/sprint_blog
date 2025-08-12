from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Главная страница блога")

def post_detail(request, id):
    return HttpResponse(f"Страница поста с id={id}")

def category_posts(request, category_slug):
    return HttpResponse(f"Посты в категории: {category_slug}")

