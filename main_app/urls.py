from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('movies/', views.movie_index, name='movie_index'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movies/create/', views.MovieCreate.as_view(), name='movie_create'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movie_update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movie_delete'),
    path('movies/<int:movie_id>/add-viewing/', views.add_viewing, name='add_viewing'),
    path('actors/create/', views.ActorCreate.as_view(), name='actor_create'),
    path('actors/<int:pk>/', views.ActorDetail.as_view(), name='actor_detail'),
    path('actors/', views.ActorList.as_view(), name='actor_index'),
    path('actors/<int:pk>/update/', views.ActorUpdate.as_view(), name='actor_update'),
    path('actors/<int:pk>/delete/', views.ActorDelete.as_view(), name='actor_delete'),
    path('movies/<int:movie_id>/associate-actor/<int:actor_id>/', views.associate_actor, name='associate_actor'),
    path('movies/<int:movie_id>/remove-actor/<int:actor_id>/', views.remove_actor, name='remove_actor'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup')
]