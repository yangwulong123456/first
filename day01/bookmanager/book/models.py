from django.db import models

# Create your models here.
class BookInfo(models.Model):

    name = models.CharField(max_length=20)


class PeopleInfo(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=100000)
    gender = models.BooleanField()
    skill = models.CharField(max_length=20)


