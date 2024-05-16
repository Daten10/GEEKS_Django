from django.urls import path
from .views import (bio_view, hobby_view, current_time_view, add_books_view, books_detail_view,
                    delete_book_view, create_book_view, edit_book_view, create_review_view)

urlpatterns = [
    path('bio/', bio_view, name='bio'),
    path('hobby/', hobby_view, name='hobby'),
    path('time/', current_time_view, name='time'),
    path('books/', add_books_view, name='books'),
    path('books/<int:id>/', books_detail_view, name='books_detail'),
    path('create_book/', create_book_view, name='create_book'),
    path('create_review/', create_review_view, name='create_review'),
    path('books/<int:id>/delete/', delete_book_view, name='delete_book'),
    path('books/<int:id>/update/', edit_book_view, name='edit_book'),

]
