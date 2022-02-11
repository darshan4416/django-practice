from django.shortcuts import redirect, render, HttpResponse
from django.core.paginator import Paginator
from .models import Book


def get_books(request):
    books = Book.objects.all()
    paginator = Paginator(books,2)

    page_number = request.GET.get('page')
    print(request.GET)
    page_obj = paginator.get_page(page_number)

    context = {'page_obj':page_obj}

    return render(request, 'index.html', context)
    
def add_books(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        pages = request.POST.get('pages')
        isbn = request.POST.get('isbn')
        print(name, author, pages, isbn)
        
        book = Book(name=name,author=author,pages=pages,isbn=isbn)
        print(name, author, pages, isbn)
        book.save()
        return redirect('get_books')

def delete_book(request, id):
    Book.objects.get(pk=id).delete()

    return redirect('get_books')

def edit_book(request, id):
    if request.method == "GET":
        book = Book.objects.get(pk=id)
        name = book.name
        author = book.author
        isbn = book.isbn
        pages = book.pages

        print(name, author, isbn, pages)

        context = {
            'id':id,
            'name':name,
            'author':author,
            'isbn':isbn,
            'pages':pages
        }

        return render(request, 'edit.html', context)
    else:
        book = Book.objects.get(pk=id)
        book.name = request.POST.get('name')
        book.author = request.POST.get('author')
        book.isbn = request.POST.get('isbn')
        book.pages = request.POST.get('pages')

        book.save()
        return redirect('get_books')

    

    



