from django.shortcuts import render
from .models import Author,Book, Librarian
from .models import Library
from django.views.generic import ListView, DetailView

# Create your views here.

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
