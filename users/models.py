from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=14, default='+996')
    age = models.PositiveIntegerField(default=18, validators=[MinValueValidator(5), MaxValueValidator(99)])
    gender = models.CharField(max_length=100, choices=GENDER)
    experience = models.PositiveIntegerField(default=0)
    telegram = models.CharField(max_length=100, blank=True)
    favorite_genre = models.CharField(max_length=100)
    club = models.CharField(max_length=100, default='новичок')


@receiver(post_save, sender=CustomUser)
def set_exp(sender, instance, created, **kwargs):
    if created:
        print('Сигнал обработан пользователь создан')
        exp = instance.experience
        if exp < 1:
            instance.club = 'Новичок'
        elif 1 <= exp <= 2:
            instance.club = 'не Новичок'
        elif 2 <= exp <= 3:
            instance.club = 'Старейшина'
        elif 3 <= exp <= 5:
            instance.club = 'Профи'
        elif exp > 5:
            instance.club = 'Книжный гуру'