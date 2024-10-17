from django.db import models


class Cake(models.Model):
    name = models.CharField(unique=True, max_length=100)
    comment = models.TextField(max_length=200)
    imageURL = models.URLField()
    yumFactor = models.IntegerField()
