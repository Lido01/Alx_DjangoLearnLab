from django.contrib import admin
from .models import Book

# Register your models here.
#@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  #  list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("title", "author", "publication_year")
    ordering = ["pk"]
    fieldsets = [
       (None, {"fields": ["title"]}),
("author", {"fields": ["publication_year"]}),]
    
admin.site.register(Book, BookAdmin)
