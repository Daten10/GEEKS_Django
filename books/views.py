from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import AddBooks


def add_books_view(request):
    if request.method == 'GET':
        book = AddBooks.objects.all().order_by('-id')
        return render(request, template_name='books.html', context={'book': book})


def books_detail_view(request, id):
    if request.method == 'GET':
        books_id = get_object_or_404(AddBooks, id=id)
        return render(request, template_name='books_detail.html', context={'books_id': books_id})


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
