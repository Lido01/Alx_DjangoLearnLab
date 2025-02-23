from django.shortcuts import render
from .models import Author,Book,Library, Librarian
from django.views.generic import ListView, DeleteView 
# Create your views here.

#Function Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'templates/list_authors.html', {'authors': authors})

# Class Based View
class BookListView(ListView):
    model = Book
    template_name = "templates/list_books.html"
    context_object_name = "book"
     
    
