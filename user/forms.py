from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.help_text = ""

        self.fields['username'].widget.attrs.update({'class':'form-control my-2'})
        self.fields['username'].widget.attrs.update({'placeholder':'Kullanıcı adı giriniz'})

        self.fields['email'].widget.attrs.update({'class':'form-control my-2'})
        self.fields['email'].widget.attrs.update({'placeholder':'Email giriniz'})

        self.fields['password1'].widget.attrs.update({'class':'form-control my-2'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Parola giriniz'})

        self.fields['password2'].widget.attrs.update({'class':'form-control my-2'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Parola tekrar giriniz'})


class ProfilForm(ModelForm):
    class Meta:
        model = Profiles
        fields = ['isim','resim']

    def __init__(self, *args, **kwargs):
        super(ProfilForm,self).__init__(*args,**kwargs)
        # for name,field in self.fields.items():
        #     field.widget.attrs.update({'class':'form-control'})

        self.fields['isim'].widget.attrs.update({
            'class':'form-control mb-3',
            'placeholder':'İsim giriniz...'
            })
        
        self.fields['resim'].widget.attrs.update({
            'class':'form-control mb-3',
            })