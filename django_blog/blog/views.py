from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from .models import Post
from rest_framework import generics
from .forms import RegistrationForm, LoginForm


def home(request):
    return render(request, 'blog/index.html')
def register(request):
    #form = UserCreationForm()
    if request.method=='POST':
        form =  RegistrationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect('login')
       # return render(request, 'templates/blog/home.html')
    else:
        form = RegistrationForm()
        #return redirect('index')
    return render(request, 'register.html', {'form': form} )

def login(request):
    if request.method =="POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

class PostView(generics.ListAPIView):
    queryset = Post.objects.all()

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()

class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
class PostDeleteView(generics.DestroyAPIView):
    
    queryset = Post.objects.all()