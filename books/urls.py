from django.urls import path
from . import views
urlpatterns = [
    path('bio/', views.bio_view, name='bio'),
    path('hobby/', views.hobby_view, name='hobby'),
    path('time/', views.current_time_view, name='time'),
    path('books/', views.AddBookView.as_view(), name='books'),
    path('books/<int:id>/', views.BooksDetailView.as_view(), name='books_detail'),
    path('create_book/', views.CreateBookView.as_view(), name='create_book'),
    path('create_review/', views.CreateReviewView.as_view(), name='create_review'),
    path('books/<int:id>/delete/', views.DeleteBookView.as_view(), name='delete_book'),
    path('books/<int:id>/update/', views.EditBookView.as_view(), name='edit_book'),
    path('search/', views.SearchBookView.as_view(), name='search')
]
