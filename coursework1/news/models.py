from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
         
class NewsStory(models.Model):
    CATEGORIES = (
        ('POL', 'Politics'),
        ('ART', 'Art News'),
        ('TECH', 'Technology'),
        ('TRIVIA', 'Trivial News')
    )
    headline = models.CharField(max_length=200)
    category = models.CharField(max_length=7, choices=CATEGORIES)
    region = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField()
    details = models.CharField(max_length=512)

    def __str__(self):
        return self.name
