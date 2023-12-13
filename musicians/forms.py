from django import forms
from .models import Musician


class AddMusiciansForms(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
