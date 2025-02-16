# commands follows with output
from bookshelf.models import Book

Book.objects # <django.db.models.manager.Manager object at 0x000001F83D0A0F50>

r =Book.objects.get(pk=1)      
r   # <Book: Book object (1)>

r.delete() # (1, {'bookshelf.Book': 1})