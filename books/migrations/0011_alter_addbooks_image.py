# Generated by Django 5.0.4 on 2024-05-26 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_addbooks_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbooks',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Загрузите фото'),
        ),
    ]
