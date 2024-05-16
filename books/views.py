from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import AddBooks
from . import forms


def create_review_view(request):
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Коментарий добавлен!')
    else:
        form = forms.ReviewForm()

    return render(request, template_name='create_review.html', context={'form': form})


def edit_book_view(request, id):
    book_id = get_object_or_404(AddBooks, id=id)
    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=book_id)
        if form.is_valid():
            form.save()
            return HttpResponse('Книга изменена!')
    else:
        form = forms.BookForm(instance=book_id)
    return render(request, template_name='edit.html', context={'book_id': book_id,
                                                               'form': form})


def delete_book_view(request, id):
    book_id = get_object_or_404(AddBooks, id=id)
    book_id.delete()
    return HttpResponse('Книга удалена')


def create_book_view(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Книга добавлена!')
    else:
        form = forms.BookForm()

    return render(request, template_name='create_book.html', context={'form': form})


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
