# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from books.models import Book


def books_list(request):
    result = "Lista ksiazek<br>"
    books = Book.objects.all()
    for book in books:
        result += f"{book}<br>"
    return render(request, 'books/list.html', {})



def book_details(request, id):
    result = "Szczegoly ksiazki<br>"
    book = Book.objects.get(id=id)
    result += "<br>"
    result += str(book)
    return HttpResponse(result)