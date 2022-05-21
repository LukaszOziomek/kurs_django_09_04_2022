from django.urls import path
from books.views import books_list, book_details

urlpatterns = [
    path("", books_list, name="list"),
    path("<int:id>", book_details, name="list"),


]