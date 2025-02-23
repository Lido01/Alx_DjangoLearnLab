from django.shortcuts import render, redirect
from .models import Author,Book, Librarian
from .models import Library

from django.views.generic import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse_lazy

#Function Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def list_authors(request):
    authors = Author.objects.all()
    return render(request, "relationship_app/list_authors.html", {'authors': authors})
    return render(request, "home/register.html", {"form": form})

# Class Based View
class BookListView(ListView):
    model = Book
    template_name = "relationship_app/list_books.html"
    context_object_name = "book"
     
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library_detail"

#Home page View
#register View
class RegisterView(View):
    template_name = 'templates/register.html'
    success_url = reverse_lazy("login")
    
    def get(self, request):
        form =  UserCreationForm()
        return render(request, 'templates/register.html', {'form': form})
    
    template_name = 'templates/register.html'
    def  post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
                user =  form.save()
                user.save()
                login(request, user)
                return redirect(self.success_url)
        else:
            form = UserCreationForm()
        return render(request, self.template_name, {"form": form})
# Login view
class Login(LoginView):
    template_name = 'templates/login.html'


