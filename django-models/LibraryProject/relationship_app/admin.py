from django.contrib import admin
from .models import Book, Author

# Register your models here.
#admin.register.s
admin.site.register(Author)

class BookAdimin(admin.ModelAdmin):
    list_display = ("title", "author")
    ordering =["pk"]

admin.site.register(Book, BookAdimin)