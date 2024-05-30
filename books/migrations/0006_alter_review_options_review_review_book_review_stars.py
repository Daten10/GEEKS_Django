# Generated by Django 5.0.4 on 2024-05-10 20:20

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0005_review"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="review",
            options={"verbose_name": "отзыв", "verbose_name_plural": "отзывы"},
        ),
        migrations.AddField(
            model_name="review",
            name="review_book",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="review_book",
                to="books.addbooks",
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="stars",
            field=models.PositiveIntegerField(
                default=5,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
    ]
