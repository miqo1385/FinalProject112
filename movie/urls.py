from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies' ),
    path('movieDetail/<int:id>', views.movieDetail, name='detail'),
    path('newreview/', views.newReview, name='newreview'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
    
]