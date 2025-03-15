from rest_framework import serializers
from .models import Book, Author
import datetime

#Author Serialization
class BookSerializer(serializers.ModelSerializer):
        def validate_publication_year(self, data): #Check if the date is valid or not
            print(datetime.date.today().year)
            if data > datetime.date.today().year:
                raise ValueError(f"The book published year out of the range!!")
            return data
        class Meta:
            model = Book
            fields = "__all__"
#Nested BookSerializer to serialize the related books dynamically
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ["name", "books"]