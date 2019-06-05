from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie


class MovieDetailView(DetailView):
    template_name = 'movies/detail.html'
    queryset = Movie.objects.all()


class MovieListView(ListView):
    template_name = 'movies/list.html'
    queryset = Movie.objects.all()