from django.shortcuts import render
from .models import Author,Book, Librarian
from .models import Library
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import  authenticate,login, logout
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

#register View
class Register(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
 
 
# Login view
class CustomLoginView(LoginView):
    template_name = 'login.html'




#Function Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'relationship/list_authors.html', {'authors': authors})

# Class Based View
class BookListView(ListView):
    model = Book
    template_name = "relationship_app/list_books.html"
    context_object_name = "book"
     
class DetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library_detail"


