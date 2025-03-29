from relationship_app.models import Author, Book, Library, Librarian
def get_books_by_author(author_name,author):
    Author.objects.get(name=author_name)
    books=Author.objects.filter(author=author)
    return books
def list_books_in_library(library_name):
    return Library.objects.get(name=library_name).books.all()
def get_librarian_for_library(library_name):
    Librarian.objects.get(library="")
    librarian=Library.objects.librarian
    return librarian