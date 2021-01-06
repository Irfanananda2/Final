from django import forms
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

    def clean_name(self):
        genre_name = self.cleaned_data.get('name')
        if (genre_name == ""):
            raise forms.ValidationError("Fill the data")
        for instance in Genre.objects.all():
            if instance.name == genre_name:
                raise forms.ValidationError(genre_name + " Already Exist")
        return genre_name     

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ['countrys']

    def clean_countrys(self):
        country_name = self.cleaned_data.get('countrys')
        if (country_name == ""):
            raise forms.ValidationError("Fill the data")
        for instance in Country.objects.all():
            if instance.countrys == country_name:
                raise forms.ValidationError(country_name + " Already Exist")
        return country_name   

class ActorForm(ModelForm):
    class Meta:
        model  = Actor
        fields = ['first_name', 'last_name', 'bio', 'bod']

class ReviewForm(ModelForm):
    class Meta:
        model  = Review
        fields = ['username', 'movie', 'review']
