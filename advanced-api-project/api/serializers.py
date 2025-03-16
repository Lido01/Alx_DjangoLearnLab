from rest_framework import serializers
from .models import Book, Author
import datetime
from django.contrib.auth.models import User


#Author Serialization
#Nested BookSerializer to serialize the related books dynamically
class AuthorSerializer(serializers.ModelSerializer):
    #books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ["name"]

class BookSerializer(serializers.ModelSerializer):
        #author = serializers.CharField(source='author.name', read_only=True)
        author = AuthorSerializer(many=True, read_only=True)
        #author_id = serializers.PrimaryKeyRelatedField(ready_only=True)
        def validate_publication_year(self, data): #Check if the date is valid or not
            print(datetime.date.today().year)
            if data > datetime.date.today().year:
                raise serializers.ValidationError(f"The book published year out of the range!!")
            return data
        
        class Meta:
            model = Book
            fields = ["title", "publication_year", "author"]