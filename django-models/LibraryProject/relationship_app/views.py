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
from django.contrib.auth.forms import UserCreationForm

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
"relationship_app/register.html"
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Role check functions
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# Views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
