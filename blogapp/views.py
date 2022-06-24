from django.shortcuts import render, redirect
from .models import Postmodel
from .forms import Postmodelform, Postupdateform
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
    return render(request, 'Blog/aboutus.html') 

def post_detail(request, pk):
    post = Postmodel.objects.get(id=pk)
    context = {
        'post':post,                
    }
    return render(request,'blog/post_detail.html',context)

def post_edit(request, pk):
    post = Postmodel.objects.get(id=pk)
    if request.method == 'POST':
        form = Postupdateform(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        form = Postupdateform(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/post_edit.html', context)

def post_delete(request, pk):
    post = Postmodel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
       
# Redirigir a home       
       
        return redirect('home')
    context = {
        'post': post
    }
    return render(request, 'blog/post_delete.html', context)