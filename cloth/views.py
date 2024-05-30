from django.shortcuts import render
from . import models
from django.views import generic


class AddClothView(generic.ListView):
    template_name = "cloth/all_cloth.html"
    context_object_name = "cloth"
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.all().order_by("-id")


class MenClothView(generic.ListView):
    template_name = "cloth/men_cloth.html"
    context_object_name = "men_cloth"
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name="мужская одежда").order_by("-id")


class WomenClothView(generic.ListView):
    template_name = "cloth/women_cloth.html"
    context_object_name = "women_cloth"
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name="женская одежда").order_by("-id")


class KidsClothView(generic.ListView):
    template_name = "cloth/kids_cloth.html"
    context_object_name = "kids_cloth"
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name="детская одежда").order_by("-id")


class SearchClothView(generic.ListView):
    template_name = "cloth/all_cloth.html"
    context_object_name = "cloth"
    paginate_by = 5

    def get_queryset(self):
        return models.Cloth.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["q"] = self.request.GET.get("q")
        return contex
