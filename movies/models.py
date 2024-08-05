from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length = 50)
    photo = models.FileField(upload_to='actors/', verbose_name="Oyuncu Fotoğrafı")

    def __str__(self):
        return self.name
    

class Kategori(models.Model):
    isim = models.CharField(max_length = 50)

    def __str__(self):
        return self.isim


class Movie(models.Model):
    isim = models.CharField(max_length = 150)
    resim = models.FileField(upload_to='filmler/', verbose_name="Film Resmi")
    video = models.FileField(upload_to='videolar/', verbose_name="Film Fragmanı")
    aciklama = models.TextField(null = True, blank = True)
    actors = models.ManyToManyField(Actor, related_name='movies', blank =True)
    kategori = models.ForeignKey(Kategori, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.isim
        

class Yorum(models.Model):
    film = models.ForeignKey(Movie, on_delete = models.CASCADE, related_name = "yorumlar")
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self,*args,**kwargs):
        if self.id:
            self.updated_at = timezone.now()
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.film.isim}"

    

