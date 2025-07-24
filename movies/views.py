from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.
def index(request):
    # SELECT * FROM movies_movie ↓
    movies = Movie.objects.all()

    # # SELECT * FROM movies_movie WHERE ↓
    # Movie.objects.filter(release_year=1985)
    # # SELECT * FROM movies_movie WHERE(single object) ↓
    # Movie.objects.get(id=1)
    
    # passing 'movies' object to index.html with {'movies': movies}
    return render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):
    # pk is primary key(id)
    movie = get_object_or_404(Movie, pk=movie_id)
    # passing 'movie' object to detail.html with {'movie': movie}
    return render(request, 'movies/detail.html', {'movie': movie})
