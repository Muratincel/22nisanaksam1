from django.forms import ModelForm
from .models import *

class YorumForm(ModelForm):
    class Meta:
        model = Yorum
        fields = ['text', 'rating']

    def __init__(self,*args,**kwargs):
        super(YorumForm,self).__init__(*args,**kwargs)

        self.fields['text'].widget.attrs.update({
            'rows':4,
            'class':'form-control',
            'placeholder':'Yorumunuzu buraya giriniz...'
            })
        
        self.fields['rating'].widget.attrs.update({
            'class':'form-control',
            'min':1,
            'max':5,
            'placeholder':'Puanınızı giriniz...'
            })