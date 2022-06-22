from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import Sign_upform, Userupdateform, ProfileupdateForm

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = Sign_upform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users/login')
   
    else:
        form=Sign_upform()    
    context = {
        'form': form, 
    }
    return render(request, 'users/sign_up.html', context)

def profile(request):
    if request.method == 'POST':
        u_form = Userupdateform(request.POST or None, instance = request.user )
        p_form = ProfileupdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect ('users-profile')
    else:
        u_form = Userupdateform(instance = request.user)
        p_form = ProfileupdateForm(instance=request.user.profilemodel)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        
    }
    return render(request, 'users/profile.html',context)