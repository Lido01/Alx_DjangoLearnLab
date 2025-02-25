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
    return render(request, "registration/register.html", {"form": form})



class LoginView(View):
    template_name = 'registration/login.html'

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
    template_name='registration/logout.html'
    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out.")
        # return redirect('login')
        return render(request, self.template_name)

def home(request):
    return render(request, "registration/home.html")


from django.contrib.auth.decorators import login_required
@login_required
def profile_view(request):
    # This view can only be accessed by authenticated users
    return render(request, 'profile.html')