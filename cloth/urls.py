from django.urls import path
from . import views


urlpatterns = [
    path("cloth_all/", views.AddClothView.as_view(), name="all_cloth"),
    path("men_cloth/", views.MenClothView.as_view(), name="men_cloth"),
    path("women_cloth/", views.WomenClothView.as_view(), name="women_cloth"),
    path("kids_cloth/", views.KidsClothView.as_view(), name="kids_cloth"),
    path("search/", views.SearchClothView.as_view(), name="search"),
]
