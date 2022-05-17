
from tkinter import Widget
from django.db import models



# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='book_cover')
    author = models.CharField(max_length=30,default='Anirudhra')
    email = models.EmailField(blank=True)
    describe = models.TextField(default='Anni Dev Books')

    def __str__(self) -> str:
        return self.name
