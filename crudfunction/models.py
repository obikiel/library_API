from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    publication_date = models.DateField()
    summary = models.CharField(max_length=1000)
    edition = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
