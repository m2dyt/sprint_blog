from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("О сайте")

def rules(request):
    return HttpResponse("Правила сайта")

