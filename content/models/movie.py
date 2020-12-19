from django.db import models
from content.models.genre import Genre
from content.models.actor import Actor
from content.models.country import Country

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    synopsis = models.TextField(max_length=1000)
    rel_date = models.DateField(null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    actor = models.ManyToManyField(Actor)
    country = models.OneToOneField('Country', on_delete=models.SET_NULL, null=True)
    

    class Meta:
        app_label = 'content'

    def __str__(self):
        return self.title