from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('movies/', views.movie_index, name='movie_index'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]