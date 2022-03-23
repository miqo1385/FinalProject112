from django import forms
from .models import MovieType, Review, Movie


class ReviewForms(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'