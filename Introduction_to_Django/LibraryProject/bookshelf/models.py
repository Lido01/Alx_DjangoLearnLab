from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()


# title = 1984
# author = George Orwell
# Publication_date = 1949
