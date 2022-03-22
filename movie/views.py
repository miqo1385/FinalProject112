from django.shortcuts import render
from .models import MovieType, Movie, Review

# Create your views here.
def index(request):
    return render(request, 'movie/index.html')

def movies(request):
    movie_list=Movie.objects.all()
    return render(request, 'movie/moviereview.html', {'movie_list': movie_list} )
