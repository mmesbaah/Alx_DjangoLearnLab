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
    from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return render(request, "logout.html")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})
