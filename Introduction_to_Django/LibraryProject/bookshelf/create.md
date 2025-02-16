# The commands
from bookshelf.models import Book

Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)

q = Book.objects
# output  <Book: Book object (None)>
q.save()
q
<Book: Book object (1)>
