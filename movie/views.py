from django.shortcuts import render,get_object_or_404
from .models import MovieType, Movie, Review
from django.urls import reverse_lazy 
from .forms import ReviewForms
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'movie/index.html')

def movies(request):
    movie_list=Movie.objects.all()
    return render(request, 'movie/moviereview.html', {'movie_list': movie_list} )

def movieDetail(request, id):
    movie=get_object_or_404(Movie, pk=id)
    return render(request, 'movie/moviedetail.html', {'movie' : movie})

@login_required
def newReview(request):
    form=ReviewForms

    if request.method=='POST':
        form=ReviewForms(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForms()
    else:
        form=ReviewForms()
    return render(request, 'movie/newreview.html', {'form' : form})

def loginmessage(request):
    return render(request, 'movie/loginmessage.html')

def logoutmessage(request):
    return render(request, 'movie/logoutmessage.html')


