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
    # return render(request, "home/register.html", {"form": form})

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
   # if request.user.is_authenticated:
   #    return redirect("home") #Prevent logged-in user from again register
    
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
    

#@permission_required(login_url= "/login/") checks if user logged or not, return to login
def home(request):
    return render(request, "relationship_app/home.html")


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
    return render(request, "templates/add_book.html", {"form": form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book(request):
    if request.method == "POST":

        title = title.request.POST.get("title")
        author = author.request.POST.get("author")
        form = Book.objects.all

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request):
    if request.method == "POST":
        form = Book.objects.get()





#Added to Admin, Librarian , Member
 # accounts/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

