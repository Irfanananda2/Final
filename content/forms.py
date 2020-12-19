from django.forms import ModelForm
from django.core.exceptions import ValidationError
from content.models import Movie,Director,Genre,Actor,Country,Review


class DirectorForm(ModelForm):
    class Meta:
        model = Director 
        fields = ['first_name', 'last_name']


class MovieForm(ModelForm):
    class Meta:
        model = Movie  
        fields = ['title', 'director', 'synopsis', 'rel_date', 'genre']

class GenreForm(ModelForm):
    class Meta:
        model = Genre 
        fields = ['name']      

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ['countrys']