from relationship_app.models import Author, Book, Library, Librarian


Book.objects # The book object

# Query all books by a specific author.
author_name1 = Author.objects.create("Gadissa")
author_name2 = Author.objects.create("Sinaf")
author_name3 = Author.objects.create("lidex")

Author.objects.get(name=author_name2)
author = Author.objects.get(id=2)
Book.objects.filter(author=author)


#Listing the book from library
library_name = Library.objects.create(name="Programming")
library_name2 = Library.objects.create(name="Financial")
library_name3 = Library.objects.create(name="Business")


li1 = Library.objects.get(name=library_name)
li2 = Library.objects.get(name=library_name3)
li2.books.all()

# Retrieve the librarian for a library.
Librarian.objects.get(library=li2)