from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html")

def movies(request):

    filmler = Movie.objects.all()
    user = request.user.kullanici

    context = {
        'filmler':filmler,
        'user': user,
    }

    return render(request, 'browse-index.html', context)

# ! Detay sayfası tasarımı
def film_detay(request, film_id):
    film = get_object_or_404(Movie, id = film_id)
    yorumlar = film.yorumlar.all()

    if request.method == "POST":
        form = YorumForm(request.POST)
        if form.is_valid():
            yorum = form.save(commit=False)
            yorum.film = film 
            yorum.user = request.user
            yorum.save()
            messages.success(request, 'Yorumun için teşekkürler!')
            return redirect('film_detay', film_id = film.id) 

    else:
        form = YorumForm()        

    context = {
        'film':film,
        'yorumlar':yorumlar,
        'form':form,
    }
    return render(request, 'film_detay.html', context)


def film_fragman(request, film_id):
    film = get_object_or_404(Movie, id = film_id)
    context = {
        'film':film
    }
    return render(request, 'film_fragman.html', context)


@login_required
def yorum_duzenle(request, yorum_id):

    yorum = get_object_or_404(Yorum, id=yorum_id)

    if yorum.user != request.user:
        return redirect('film_detay', film_id = yorum.film.id)

    if request.method == "POST":
        form = YorumForm(request.POST, instance = yorum)
        if form.is_valid():
            form.save()
            messages.success(request, 'Yorumun başarıyla güncellendi!')
            return redirect('film_detay', film_id = yorum.film.id)
    
    else:
        form = YorumForm(instance = yorum)

    context = {
        'yorum':yorum,
        'form':form
    }

    return render(request, 'yorum_duzenle.html', context)


@login_required
def yorum_sil(request, yorum_id):
    yorum = get_object_or_404(Yorum, id = yorum_id)

    if yorum.user == request.user:
        film_id = yorum.film.id
        yorum.delete()
        messages.success(request, 'Yorum silindi!')
        return redirect('film_detay', film_id = yorum.film.id)
    
    else:
        return redirect('film_detay', film_id = yorum.film.id)
