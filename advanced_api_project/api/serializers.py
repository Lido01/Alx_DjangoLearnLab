from rest_framework import serializers
from .models import Book, Author
import time

#Author Serialization
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        def validate(self, data): #Check if the date is valid or not
            if self.publication_year < "current year":
                raise ValueError("The book published year out of day(it say future!!)")
            return data
#Nested BookSerializer to serialize the related books dynamically
class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ["name", "book"]