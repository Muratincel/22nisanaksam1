from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def userRegister(request):

    # form = UserForm()
    # if request.method == "POST":
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Başarıyla kayıt olundu!')
    #         return redirect('index')
    #     else:
    #         return redirect('register')

    # context = {
    #     'form':form
    # }

    if request.method == "POST":
        kullaniciAdi = request.POST['kullaniciAdi']
        isim = request.POST['isim']
        soyisim = request.POST['soyisim']
        email = request.POST['email']
        resim = request.FILES.get('resim', None)
        tel = request.POST['tel']
        dogum = request.POST['dogum']
        sifre1 = request.POST.get('sifre1')
        sifre2 = request.POST.get('sifre2')

        if sifre1 == sifre2:
            if User.objects.filter(email = email).exists():
                messages.error(request, 'Bu mail adresi zaten kullanılmakta!')
                return redirect('register')
            
            elif len(sifre1) < 6:
                messages.error(request, "Şifreniz 6 karakterden kısa olamaz!")
                return redirect('register')
            
            elif len(isim) < 6:
                messages.error(request, "İsim 6 karakterden kısa olamaz!")
                return redirect('register')

            else:
                user = User.objects.create_user(username=kullaniciAdi, email=email, password=sifre1)

                Kullanici.objects.create(
                    user=user,
                    kullaniciAdi = kullaniciAdi,
                    isim = isim,
                    soyisim = soyisim,
                    resim = resim,
                    email = email,
                    tel = tel,
                    dogum = dogum
                )

                user.save()

                #! Email islemleri
                subject = "basarili yeni kayit"
                message = f"hosgeldiniz {isim} {soyisim}. kayit isleminiz basariyla tamamlanmistir"
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]

                send_mail(subject, message, from_email, recipient_list)

                messages.success(request, 'Kullanıcı Oluşturuldu!. mail kutunuzu kontrol ediniz')
                return redirect('login')
            
    return render(request, "register.html")


def userLogin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Başarıyla giriş yapıldı!')
            return redirect('profiles')
        else:
            messages.error(request, "Kullanıcı adı ya da şifre hatalı!")
            return redirect('login')

    return render(request, 'login.html')


def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış Yapıldı!')
    return redirect('index')


def profiles(request):

    profiller = Profiles.objects.filter(owner = request.user)

    context = {
        'profiller': profiller
    }

    return render(request, 'browse.html', context)


def createProfil(request):
    form = ProfilForm()

    mevcut_profil_sayisi = Profiles.objects.filter().count()
    max_profil_sayisi = 4

    if mevcut_profil_sayisi >= max_profil_sayisi:
        messages.error(request, 'Profil sayısını aştınız!')
        return redirect('profiles')

    if request.method == "POST":
        form = ProfilForm(request.POST, request.FILES)
        if form.is_valid():
            profil = form.save(commit=False)
            profil.owner = request.user
            profil.save()
            messages.success(request, 'Profil başarıyla oluşturuldu!')
            return redirect('profiles')
    
    context = {
        'form':form
    }

    return render(request, "create.html", context)


def delete_profile(request, profile_id):
    profile = get_object_or_404(Profiles, id = profile_id)

    if request.method == "POST":
        profile.delete()
        messages.success(request, 'Profil başarıyla silindi!')
        return redirect('profiles')
    
    context = {
        'profile':profile
    }

    return render(request, "delete_profile.html", context)



def edit_profile(request, profile_id):

    profile = Profiles.objects.get(id = profile_id)

    if request.method == "POST":
        form = ProfilForm(request.POST, request.FILES, instance = profile)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profil başarıyla düzenlendi!')
            return redirect('profiles')
    
    else:
        form = ProfilForm(instance = profile)

    context = {
        'form':form,
        'profile':profile
    }

    return render(request, 'edit_profile.html', context)


def hesap(request):

    user = request.user.kullanici

    context = {
        'user':user
    }

    return render(request, 'hesap.html', context)

def passwordChange(request):

    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "sifre degistirme islemi basarili")
            return redirect('login')
        else:
            messages.error(request, "bilgiler hatali")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
    }        
    
    return render(request, "password_change.html", context)

def account_delete(request):
    user = request.user

    if request.method == "POST":
        if user.is_authenticated:
            user = request.user
            user.delete()
            logout(request)
            messages.success(request, "hesabiniz silindi")
            return redirect('index')
        else:
            messages.error(request, "hesabinizi silmek icini girisli olmak zorundasiniz")
            return redirect('login')
    
    return redirect('hesap')