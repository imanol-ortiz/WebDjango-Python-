from django import forms
from .models import Postmodel,comment

class Postmodelform(forms.ModelForm):
    contenido= forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    class Meta:
        model = Postmodel
        fields = ('titulo','contenido')


class Postupdateform(forms.ModelForm):
    class Meta:
        model = Postmodel
        fields = ('titulo', 'contenido')
        
class commentform(forms.ModelForm):
    content= forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'Agregar comentario....'}))
    class Meta:
        model = comment
        fields = ('content',)