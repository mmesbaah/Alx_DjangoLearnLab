from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    
    
# This Python class defines a model for a Book object with attributes such as title, author (linked to
# another model Author), and publication year.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    
    search_fields = ['title', 'author']
    ordering = ['title', 'publication_year']
    
    def __str__(self):
        return self.title

class Author(models.Model), class Book(models.Model)