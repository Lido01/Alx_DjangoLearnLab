from django.shortcuts import render, redirect
from .models import Author,Book, Librarian
from .models import Library
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .forms import Bookform

#Function Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def list_authors(request):
    authors = Author.objects.all()
    return render(request, "relationship_app/list_authors.html", {'authors': authors})

# Class Based View
class BookListView(ListView):
    model = Book
    template_name = "relationship_app/list_books.html"
    context_object_name = "book"
     
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library_detail"

# Function Based registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("registered succesffuly")
            login(request, user)
            messages.error(request, "Registration is successful! You can now login")
            return redirect('login')
        else:
            messages.error(request, "Invalid input, Please make Sure before submit to register!!")

    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

class LoginView(View):
    template_name = 'relationship_app/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login is successful")
            return redirect("home")
        else:
            messages.error(request, "Incorrect input. Please make sure before submitting!")
        
        return render(request, self.template_name)

class LogoutView(View):
    template_name='relationship_app/logout.html'
    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out.")
        # return redirect('login')
        return render(request, self.template_name)
    

def home(request):
    return render(request, "relationship_app/home.html")

#Added to Admin, Librarian , Member view
 # accounts/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def is_admin(user):
    user.userprofile.role == "Admin"

def is_librarian(user):
    user.userprofile.role == "Librarian"

def is_member(user):
    user.userprofile.role == "Member"

@user_passes_test(is_admin, login_url="login")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian, login_url="login")
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member, login_url="login")
def member_view(request):
    return render(request, "relationship_app/member_view.html")



#Book Permissions that added
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    form = Bookform()
    if request.method == "POST":
        form = Bookform(request.POST)
        # title = title.request.POST.get("title")
        # author = author.request.Post.get("author")
        if form.is_valid:
            form.save()
            return redirect("book_list")
        else:
            form = Bookform()
            """return render(request, "templates/add_book.html", {"error": "Book not added"})"""
    return render(request, "relationship_app/add_book.html", {"form": form})


@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = Bookform(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list', pk=book.pk)  # Redirect to the book detail view
    else:
        form = Bookform(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to a book list or detail view
    return render(request, 'relationship_app/delete_book.html', {'book': book})





