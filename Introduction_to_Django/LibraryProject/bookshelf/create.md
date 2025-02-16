# The commands
from bookshelf.models import Book

q = Book(title = "1984", author = "George Orwell", publication_year="1949")

q
# output  <Book: Book object (None)>
q.save()
q
<Book: Book object (1)>
