from django.shortcuts import render, redirect 
from .models import Book
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm


# Create your views here.
def  MyView(request):
    context = {
        "username": "b"
    }
    # if request.user.has_perm('app_name.add_post'):
    #     redirect(request, "templates/add_book,html")
    # else:
    #     redirect(request, "templates/book_list.html")
    return render(request, "templates/index.html", context)

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, 'templates/edit_page.html', context)


