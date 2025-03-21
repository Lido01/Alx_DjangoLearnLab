from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from .models import Post
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import RegistrationForm, LoginForm, ProfileForm

#1 User Authentication
def home(request):
    return render(request, 'blog/home.html')
def register(request):
    #form = UserCreationForm()
    if request.method=='POST':
        form =  RegistrationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
        #return redirect('index')
    return render(request, 'blog/register.html', {'form': form} )

def login(request):
    if request.method =="POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = LoginForm()
    return render(request, "blog/login.html", {"form": form})


#2 profile Management
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})


#3 Post CRUD operations
class ListView(generics.ListAPIView):
    model = Post
    template_name = 'post_list.html'  # HTML template
    context_object_name = 'posts'    # Default variable for the template

class CreateView(LoginRequiredMixin, generics.CreateAPIView):
    #queryset = Post.objects.all()
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the logged-in user as the author
        return super().form_valid(form)

 # Detail View: Display a single post
class DetailView(generics.RetrieveAPIView):
    model = Post
    template_name = 'post_detail.html'
    
class UpdateView(generics.UpdateAPIView):
    #queryset = Post.objects.all()
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
 # Delete View: Allow authors to delete their posts
class DeleteView(LoginRequiredMixin, UserPassesTestMixin, generics.DestroyAPIView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author