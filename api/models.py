from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)

    def __repr__(self):
        return f'{self.title} - {self.author}'

    def __str__(self):
        return f'{self.title} - {self.author}'
