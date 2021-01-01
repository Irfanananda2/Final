from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from content.models.director import Director
from content.models.movie import Movie
from content.models.genre import Genre
from content.models.actor import Actor
from content.models.country import Country


def index(request):
    num_movies = Movie.objects.all().count()
    num_directors = Director.objects.all().count()
    num_genres = Genre.objects.all().count()
    num_actors = Actor.objects.all().count()
    num_countries = Country.objects.all().count()
    context = {
        'num_movies': num_movies,
        'num_directors': num_directors,
        'num_genres': num_genres,
        'num_actors': num_actors,
        'num_countries': num_countries,
    }
    return render(request, 'index.html', context=context)