from relationship_app.models import Author, Book, Library


"""
    
    Query all books by a specific author.
    List all books in a library.
    Retrieve the librarian for a library.
    
    """

Book.objects.all()
b1 = Book.objects.all()
b1.save()
Book.objects.all().values()
