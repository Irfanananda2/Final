from django.db import models
from content.models.movie import Movie


class Review(models.Model):
    username = models.CharField(max_length=100, blank=False)
    movie = models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True, blank=False)
    review = models.TextField(max_length=5000, blank=False)

    class Meta:
        app_label = 'content'

    def __str__(self):
        return f'{self.username}, {self.movie}'