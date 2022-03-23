from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MovieType(models.Model):
    moviegender=models.CharField(max_length=255)
    moviedescription=models.TextField(null=True, blank=True)


    def __str__(self):
        return self.moviegender
    class Meta:
        db_table='movietype'


class Movie(models.Model):
    moviename=models.CharField(max_length=255)
    moviegender=models.ForeignKey(MovieType, on_delete=models.DO_NOTHING )
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateentered=models.DateField()
    datemoviereleased=models.DateField()
    moviebudget=models.DecimalField(max_digits=10, decimal_places=2)
    producturl=models.URLField()



    def __str__(self):
        return self.moviename

    class Meta:
        db_table='movie'


class Review(models.Model):
    movietitle=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    reviewdate=models.DateField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.movietitle

    class Meta:
        db_table='review'



