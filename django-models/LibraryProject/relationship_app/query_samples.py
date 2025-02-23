from relationship_app.models import Author, Book, Library, Librarian


Book.objects # The book object
# Query all books by a specific author.
author_name = Author.objects.create("Gadissa")
author_name2 = Author.objects.create("Sinaf")
Author.objects.get(name=author_name)
author = Author.objects.get(id=1)
Book.objects.filter(author=author)


#Listing the book from library
library_name = Library.objects.create(name="Programming")
library_name2 = Library.objects.create(name="Financial")
library_name3 = Library.objects.create(name="Business")


library1 = Library.objects.get(name=library_name)
library1.books.all()

# Retrieve the librarian for a library.
Librarian.objects.get(library=library1)