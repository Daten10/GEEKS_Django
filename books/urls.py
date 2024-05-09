from django.urls import path
from .views import bio_view, hobby_view, current_time_view, add_books_view, books_detail_view

urlpatterns = [
    path('bio/', bio_view, name='bio'),
    path('hobby/', hobby_view, name='hobby'),
    path('time/', current_time_view, name='time'),
    path('books/', add_books_view, name='books'),
    path('books/<int:id>/', books_detail_view, name='books_detail'),

]
