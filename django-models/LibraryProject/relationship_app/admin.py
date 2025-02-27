from django.contrib import admin
from .models import Book, Author, UserProfile

# Register your models here.
#admin.register.s
admin.site.register(Author)

class BookAdimin(admin.ModelAdmin):
    list_display = ("title", "author")
    ordering =["pk"]

admin.site.register(Book, BookAdimin)

admin.site.register(UserProfile)