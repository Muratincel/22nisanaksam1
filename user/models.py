from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profiles(models.Model):
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    isim = models.CharField(max_length = 50)
    resim = models.FileField(upload_to='profiles/', verbose_name="Profil Resmi")

    def __str__(self):
        return self.isim
    

class Kullanici(models.Model):
    kullaniciAdi = models.CharField(max_length = 50, null=True, blank = True)
    isim = models.CharField(max_length = 50)
    soyisim = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100, null = True, blank = True)
    resim = models.FileField(upload_to='kullanicilar/', verbose_name="Profil Resmi")
    tel = models.IntegerField(default = 0)
    dogum = models.DateField()
    olusturulma_tarih = models.DateTimeField(auto_now_add = True, editable= False)
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.isim
    