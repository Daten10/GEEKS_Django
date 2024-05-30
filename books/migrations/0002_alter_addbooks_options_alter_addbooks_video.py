# Generated by Django 5.0.4 on 2024-05-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="addbooks",
            options={"verbose_name": "книга(у)", "verbose_name_plural": "книг(и)"},
        ),
        migrations.AlterField(
            model_name="addbooks",
            name="video",
            field=models.URLField(
                blank=True, null=True, verbose_name="Укажите видео ссылку"
            ),
        ),
    ]
