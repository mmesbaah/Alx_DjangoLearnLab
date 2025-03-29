from django.shortcuts import render
from .models import Book
def list_books(request):
    books = book.objects.all()
    return render(request, "list_books.html", {"books": books})

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
