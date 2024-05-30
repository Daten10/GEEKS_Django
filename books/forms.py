from django import forms
from . import models


class BookForm(forms.ModelForm):

    class Meta:
        model = models.AddBooks
        fields = [
            "title",
            "author",
            "image",
            "description",
            "book_genre",
            "price",
            "key_words",
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ["review_book", "stars", "text"]
