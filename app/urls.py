from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
   path('',get_books,name="get_books"),
   path('add-books/',add_books),
   path('delete-book/<int:id>/',delete_book),
   path('edit-book/<int:id>/',edit_book)
]
