from django.urls import path
from . import views


urlpatterns = [
    path('cloth_all/', views.all_cloth, name='all_cloth'),
    path('men_cloth/', views.men_cloth, name='men_cloth'),
    path('women_cloth/', views.women_cloth, name='women_cloth'),
    path('kids_cloth/', views.kids_cloth, name='kids_cloth'),
]

