from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def bio_view(request):
    if request.method == 'GET':
        return HttpResponse('Я Данил Тен, мне 19 лет')


def hobby_view(request):
    if request.method == 'GET':
        return HttpResponse('Моё хобби это спать')


def current_time_view(request):
    if request.method == 'GET':
        current_time = datetime.now().time()
        return HttpResponse(current_time)
