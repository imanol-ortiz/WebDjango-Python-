from attr import fields
from django import forms
from .models import Postmodel

class Postmodelform(forms.ModelForm):
    contenido= forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    class Meta:
        model = Postmodel
        fields = ('titulo','contenido')