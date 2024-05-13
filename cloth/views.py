from django.shortcuts import render
from . import models


def all_cloth(request):
    if request.method == 'GET':
        cloth = models.Cloth.objects.all().order_by('-id')
        return render(request, template_name='cloth/all_cloth.html', context={'cloth': cloth})


def men_cloth(request):
    if request.method == 'GET':
        men_cloth = models.Cloth.objects.filter(tags__name='мужская одежда').order_by('-id')
        return render(request, template_name='cloth/men_cloth.html', context={'men_cloth': men_cloth})


def women_cloth(request):
    if request.method == 'GET':
        women_cloth = models.Cloth.objects.filter(tags__name='женская одежда').order_by('-id')
        return render(request, template_name='cloth/women_cloth.html', context={'women_cloth': women_cloth})


def kids_cloth(request):
    if request.method == 'GET':
        kids_cloth = models.Cloth.objects.filter(tags__name='детская одежда').order_by('-id')
        return render(request, template_name='cloth/kids_cloth.html', context={'kids_cloth': kids_cloth})

