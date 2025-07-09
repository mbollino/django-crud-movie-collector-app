from django.shortcuts import render
from django.http import HttpResponse

class Movie:
    def __init__(self, title, director, genre, year):
        self.title = title
        self.director = director
        self.genre = genre
        self.year = year

movies = [
    Movie("Inception", "Christopher Nolan", "Sci-Fi", 2010),
    Movie("The Godfather", "Francis Ford Coppola", "Crime", 1972),
    Movie("Pulp Fiction", "Quentin Tarantino", "Crime", 1994),
    Movie("The Dark Knight", "Christopher Nolan", "Action", 2008),
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello!</h1>')

def about(request):
    return render(request, 'about.html')

def movie_index(request):
    return render(request, 'movies/index.html', {'movies': movies})