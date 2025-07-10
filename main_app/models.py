from django.db import models
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'movie_id': self.id})