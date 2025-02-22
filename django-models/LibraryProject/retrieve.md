from bookshelf.models import Book

"""Book.objects
retrive = Book.objects.all()"""
retrive # <QuerySet [<Book: Book object (1)>]>

r =Book.objects.get(pk=1) # <Book: Book object (1)>


r # <Book: Book object (1)>



