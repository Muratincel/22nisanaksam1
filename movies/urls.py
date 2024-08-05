from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('movies/', movies, name="movies"),
    path('film/<int:film_id>', film_detay, name="film_detay"),
    path('film/<int:film_id>/fragman', film_fragman, name="film_fragman"),
    path('yorum/<int:yorum_id>/duzenle/', yorum_duzenle, name="yorum_duzenle"),
    path('yorum/<int:yorum_id>/sil/', yorum_sil, name="yorum_sil"),
]