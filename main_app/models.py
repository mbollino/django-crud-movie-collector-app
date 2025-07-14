from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

PERSONAL_RATING = (
    (1, '1 Star'),
    (2, '2 Stars'),
    (3, '3 Stars'),
    (4, '4 Stars'),
    (5, '5 Stars'),
)

GENDER_CHOICES = (
    ('', 'Select a gender'),
    ('M', 'Male'),
    ('F', 'Female'),
    ('NB', 'Non-Binary'),
    ('O', 'Other'),    
)

class Actor(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=GENDER_CHOICES[0][0]
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={'pk': self.id})

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField(blank=True)

    actors = models.ManyToManyField(Actor, related_name='movies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'movie_id': self.id})
    
class Viewing(models.Model):
    view_date = models.DateField()
    personal_rating = models.IntegerField(
        choices=PERSONAL_RATING, 
        default=PERSONAL_RATING[0][0]
    )

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='viewings')

    def __str__(self):
        return f"{self.view_date} - {self.get_personal_rating_display()}"
    
    class Meta:
        ordering = ['-view_date']

    def related_actors(self):
        return self.movie.actors.all()

