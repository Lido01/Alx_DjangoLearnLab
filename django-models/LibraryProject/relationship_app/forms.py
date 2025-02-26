from django import forms
from .views import Book

class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]