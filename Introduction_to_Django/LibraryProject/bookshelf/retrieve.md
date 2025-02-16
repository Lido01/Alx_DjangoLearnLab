from bookshelf.models import Book

Book.objects # <django.db.models.manager.Manager object at 0x000001F83D0A0F50>

retrive = Book.objects.all()
retrive # <QuerySet [<Book: Book object (1)>]>

r =Book.objects.get(pk=1) # <Book: Book object (1)>


r # <Book: Book object (1)>



