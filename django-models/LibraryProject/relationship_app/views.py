from django.shortcuts import render
from .models import Book
def list_books(request):
    books = book.objects.all()
    "relationship_app/list_books.html", "Book.objects.all()"
    return render(request, "list_books.html", {"books": books})

from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    "relationship_app/library_detail.html"
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
