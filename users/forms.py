from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

GENDER = (("Male", "Male"), ("Female", "Female"))


class CustomRegistrationForm(UserCreationForm):
    name = forms.CharField(required=True)
    surname = forms.CharField(required=True)
    city = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    experience = forms.IntegerField(required=True)
    telegram = forms.CharField(required=True)
    favorite_genre = forms.CharField(required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "name",
            "surname",
            "city",
            "gender",
            "phone_number",
            "age",
            "experience",
            "telegram",
            "favorite_genre",
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


@receiver(post_save, sender=models.CustomUser)
def set_exp(sender, instance, created, **kwargs):
    if created:
        print("Сигнал обработан пользователь создан")
        exp = instance.experience
        if exp < 1:
            instance.club = "Новичок"
        elif 1 <= exp <= 2:
            instance.club = "не Новичок"
        elif 2 <= exp <= 3:
            instance.club = "Старейшина"
        elif 3 <= exp <= 5:
            instance.club = "Профи"
        elif exp > 5:
            instance.club = "Книжный гуру"
