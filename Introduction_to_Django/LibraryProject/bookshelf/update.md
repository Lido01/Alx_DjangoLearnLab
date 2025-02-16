from bookshelf.models import Book

q = Book.objects.all()[0]
q.title # "1984"


q.title = "Nineteen Eighty-Four"
q.save()

q.title  #  'Nineteen Eighty-Four'


