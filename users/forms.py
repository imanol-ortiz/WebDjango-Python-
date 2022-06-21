from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profilemodel
from django import forms

class Sign_upform(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
    def __init__(self, *args, **kwargs):
        super(Sign_upform, self).__init__(*args, **kwargs)
            
        for fieldname in ['username','email','password1','password2']:
            self.fields[fieldname].help_text = None

class Userupdateform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
    
    def __init__(self, *args, **kwargs):
        super(Userupdateform, self).__init__(*args, **kwargs)
            
        for fieldname in ['username','email',]:
            self.fields[fieldname].help_text = None

class ProfileupdateForm(forms.ModelForm):
    class Meta:
        model = Profilemodel
        fields = ['image']