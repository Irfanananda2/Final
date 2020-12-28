from django.urls import path
from content.controllers import index_controller, director_controller, movie_controller, genre_controller, actor_controller, country_controller


urlpatterns = [
    path('', index_controller.index, name='index'),
    path('directors/', director_controller.list_directors, name='directors'),
    path('director/add', director_controller.add_director, name='add_director'),
    path('director/edit/<int:director_id>', director_controller.edit_director, name='edit_director'),
    path('author/delete/<int:director_id>', director_controller.delete_director, name='delete_director'),
    path('movies/', movie_controller.list_movies, name='movies'),
    path('movie/add', movie_controller.add_movie, name='add_movie'),
    path('movie/edit/<int:movie_id>', movie_controller.edit_movie, name='edit_movie'),
    path('movie/delete/<int:movie_id>', movie_controller.delete_movie, name='delete_movie'),
    path('genres/', genre_controller.list_genres, name='genres'),
    path('genre/add', genre_controller.add_genre, name='add_genre'),
    path('genre/edit/<int:genre_id>', genre_controller.edit_genre, name='edit_genre'),
    path('genre/delete/<int:genre_id>', genre_controller.delete_genre, name='delete_genre'),
    path('actor/', actor_controller.list_actor, name='actors'),
    path('actor/add', actor_controller.add_actor, name='add_actor'),
    path('actor/edit/<int:actor_id>', actor_controller.edit_actor, name='edit_actor'),
    path('actor/delete/<int:actor_id>', actor_controller.delete_actor, name='delete_actor'),
    path('country/', country_controller.list_country, name='countrys'),
    path('country/add', country_controller.add_country, name='add_country'),
    path('country/edit/<int:country_id>', country_controller.edit_country, name='edit_country'),
    path('country/delete/<int:country_id>', country_controller.delete_country, name='delete_country'),
]
