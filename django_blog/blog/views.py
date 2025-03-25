from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from .models import Post, Comment
from taggit.models import Tag
#from rest_framework import generics
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import RegistrationForm, LoginForm, ProfileForm, CommentForm, PostForm
from django.db.models import Q
from django.views.generic import TemplateView
from django.contrib import messages


#1 User Authentication
#@login_required
# def home(request):
#     return render(request, 'blog/home.html')
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "blog/home.html"
    login_url = "login" # URL where unauthenticated users are redirected
    
    # Override the no-permission handler to add an error message
    def handle_no_permission(self):
        messages.error(self.request, "You must log in to access the home page.")
        return super().handle_no_permission()

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
            return redirect("home")
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
    return render(request, 'blog/profile.html', {'form':form})


#3 Post CRUD operations
class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'  # HTML template
    context_object_name = 'posts'  # Allows you to refer to the list of posts in the template using . 

class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user  # Assign the logged-in user as the author
        return super().form_valid(form)
    def get_success_url(self):
        print("Redirecting to post_list...")
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


class SearchView(generic.ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'results'
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return Post.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) | 
            Q(tags__name__icontains=query)
        ).distinct()

class PostsByTagView(generic.ListView):
    model = Post
    template_name = 'posts_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Retrieve the tag name from the URL pattern
        tag_name = self.kwargs.get('tag_name')
        # Fetch the tag object (or 404 if it doesn't exist)
        tag = get_object_or_404(Tag, name=tag_name)
        # Filter posts associated with the specified tag
        return Post.objects.filter(tags=tag)
    
    def get_context_data(self, **kwargs):
        # Add additional context to the template (e.g., the tag name)
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs.get('tag_name')
        return context