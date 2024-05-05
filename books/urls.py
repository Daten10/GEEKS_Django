from django.urls import path
from .views import bio_view, hobby_view, current_time_view

urlpatterns = [
    path('bio/', bio_view, name='bio'),
    path('hobby/', hobby_view, name='hobby'),
    path('time/', current_time_view, name='time'),
]
