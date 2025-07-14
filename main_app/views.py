from django.shortcuts import render, redirect
from django.db.models import Avg
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Movie, Actor, Viewing
from .forms import ViewingForm

# Create your views here.
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('movie_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class Home(LoginView):
    template_name = 'home.html'

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def movie_index(request):
    movies = Movie.objects.filter(user=request.user)
    return render(request, 'movies/index.html', {'movies': movies})

@login_required
def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    actors_movie_doesnt_have = Actor.objects.exclude(id__in = movie.actors.all().values_list('id'))
    viewing_form = ViewingForm()
    viewings = movie.viewings.all()
    return render(request, 'movies/detail.html', { 
        'movie': movie, 
        'viewing_form': viewing_form,
        'actors': actors_movie_doesnt_have,
        'viewings': viewings,
        })

class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'director', 'release_year', 'genre', 'rating', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = ['title', 'director', 'release_year', 'genre', 'rating', 'description']

class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    success_url = '/movies/'

    def get_success_url(self):
        return self.success_url

@login_required    
def add_viewing(request, movie_id):
    form = ViewingForm(request.POST)
    if form.is_valid():
        new_viewing = form.save(commit=False)
        new_viewing.movie_id = movie_id
        new_viewing.save()

        print(f"Viewing for movie '{new_viewing.movie.title}' added on {new_viewing.view_date}")

    return redirect('movie_detail', movie_id=movie_id)

class ActorCreate(LoginRequiredMixin, CreateView):
    model = Actor
    fields = '__all__'

class ActorList(LoginRequiredMixin, ListView):
    model = Actor
    context_object_name = 'actors'
    template_name = 'actors/actor_index.html'

class ActorDetail(LoginRequiredMixin, DetailView):
    model = Actor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actor = self.get_object() 
        context['movies'] = actor.movies.all()
        context['viewings'] = Viewing.objects.filter(movie__actors=actor)
        return context
    
class ActorUpdate(LoginRequiredMixin, UpdateView):
    model = Actor
    fields = ['name', 'gender']

class ActorDelete(LoginRequiredMixin, DeleteView):
    model = Actor
    success_url = '/actors/'

@login_required
def associate_actor(request, movie_id, actor_id):
    Movie.objects.get(id=movie_id).actors.add(actor_id)
    return redirect('movie_detail', movie_id=movie_id)

@login_required
def remove_actor(request, movie_id, actor_id):
    Movie.objects.get(id=movie_id).actors.remove(actor_id)
    return redirect('movie_detail', movie_id=movie_id)
