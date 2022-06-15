from django.shortcuts import render, redirect
from .models import Postmodel
from .forms import Postmodelform
# Create your views here.

def home(request):
    posts = Postmodel.objects.all()
    if request.method == 'POST':
        form = Postmodelform(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form =Postmodelform
    form =Postmodelform()
    context ={
        'posts':posts,
        'form':form,
    }
    
    return render(request, 'Blog/home.html', context)

def about(request):
    return 