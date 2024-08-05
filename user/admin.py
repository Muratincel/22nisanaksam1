from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profiles)

@admin.register(Kullanici)
class KullaniciAdmin(admin.ModelAdmin):
    list_display = ('kullaniciAdi','isim','soyisim','email','olusturulma_tarih')