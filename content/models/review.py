from django.db import models
from content.models.movie import Movie


class Review(models.Model):
    username = models.CharField(max_length=100)
    movie = models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True)
    review = models.TextField(max_length=5000)

    class Meta:
        app_label = 'content'

    def __str__(self):
        return f'{self.username}, {self.movie}'