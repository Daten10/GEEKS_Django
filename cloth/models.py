from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cloth(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/cloth/", blank=True)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=500)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
