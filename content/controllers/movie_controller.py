from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from content.models.movie import Movie
from content.forms import MovieForm

def list_movies(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movie/movies.html', context=context)

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('movies'))
    else:
        form = MovieForm()

    context = {
        'form': form
    }
    return render(request, 'movie/movie_form.html', context=context)


def edit_movie(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_id)
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('movies'))
    else:
        movie = Movie.objects.get(pk=movie_id)
        fields = model_to_dict(movie)
        form = MovieForm(initial=fields, instance=movie)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'movie/movie_form.html', context=context)


def delete_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'POST':
        movie.delete()
        return HttpResponseRedirect(reverse('movies'))
    context = {
        'movie': movie,
    }
    return render(request, 'movie/movie_delete_form.html', context=context)