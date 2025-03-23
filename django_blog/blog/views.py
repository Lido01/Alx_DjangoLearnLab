from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from .models import Post, Comment
#from rest_framework import generics
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import RegistrationForm, LoginForm, ProfileForm, CommentForm

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
class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'  # HTML template
    context_object_name = 'posts'  # Allows you to refer to the list of posts in the template using . 

class PostCreateView(generic.CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Assign the logged-in user as the author
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('post_list')  # Redirect to the list of posts after creation


 # Detail View: Display a single post
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = "post" # Refers to the individual post in the template.
     
class PostUpdateView(generic.UpdateView):
    #queryset = Post.objects.all()
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    def get_success_url(self):
        return reverse_lazy('post_list')  # Redirect after updating

 # Delete View: Allow authors to delete their posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    def get_success_url(self):
        return reverse_lazy('post_list')  # Redirect after deletion


# Comment Views
class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs['post_id'])
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['post_id']})

class CommentUpdateView(generic.UpdateView):
    model = Comment
    template_name = "blog/comment/comment_update.html"
    fields = ["content"]

class CommentDeleteView(generic.DeleteView):
    model = Comment
    template_name = ["blog/comment/comment_delete_confirmation.html"]
    fields = ["content"]


