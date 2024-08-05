from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Movie)
# admin.site.register(Actor)
# admin.site.register(Kategori)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('isim', 'resim', 'video', 'kategori')
    filter_horizontal = ('actors',)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo')

@admin.register(Yorum)
class YorumAdmin(admin.ModelAdmin):
    list_display = ('user','film','rating','created_at')
    search_fields = ('user__username', 'film__isim')

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('isim',)