from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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