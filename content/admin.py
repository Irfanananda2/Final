from django.contrib import admin
from content.models import Director, Movie, Genre, Actor, Country, Review


admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Country)
admin.site.register(Review)
