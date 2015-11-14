#-*-coding:utf-8-*-
from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorID = models.CharField(max_length=30,primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    country = models.CharField(max_length=30)
    def __unicode__(self):
	    return self.name
class Book(models.Model):
    ISBN = models.CharField(max_length=30,primary_key=True)
    title = models.CharField(max_length=30)
    AuthorID = models.ForeignKey(Author)
    publisher = models.CharField(max_length=30)
    publishdate = models.DateField()
    price = models.FloatField()
    def __unicode__(self):
	    return self.title