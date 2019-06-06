from django.db import models

class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True) 
#    publisher = models.ForeignKey(max_length=10)
    publisher_date = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False)
    isbn = models.CharField(max_length=40, blank= True, null = True)
    number_pages = models.IntegerField( default=1 )
    bookbinding = models.CharField(max_length=20, blank= True, null = True)
    genre = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    

class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    death_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

class Publisher(models.Model):
    name = models.CharField(max_length=50)

class Genre(models.Model):
     name = models.CharField(max_length=30)
