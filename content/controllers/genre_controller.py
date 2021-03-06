from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from content.models.genre import Genre
from content.forms import GenreForm
from django.contrib.auth.decorators import login_required

def list_genres(request):
    if request.method == 'POST':
        req = request.POST.dict()
        name = req['name']
        genres = Genre.objects.filter(name__contains=name)
    else:
        genres = Genre.objects.all()
    context = {
        'genres': genres,
    }
    return render(request, 'genre/genres.html', context=context)

@login_required
def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('genres'))
    else:
        form = GenreForm()

    context = {
        'form': form
    }
    return render(request, 'genre/genre_form.html', context=context)

@login_required
def edit_genre(request, genre_id):
    if request.method == 'POST':
        genre = Genre.objects.get(pk=genre_id)
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('genres'))
    else:
        genre = Genre.objects.get(pk=genre_id)
        fields = model_to_dict(genre)
        form = GenreForm(initial=fields, instance=genre)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'genre/genre_form.html', context=context)

@login_required
def delete_genre(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    if request.method == 'POST':
        genre.delete()
        return HttpResponseRedirect(reverse('genres'))
    context = {
        'genre': genre
    }
    return render(request, 'genre/genre_delete_form.html', context=context)