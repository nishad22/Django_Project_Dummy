import re
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Book
# Create your views here.



def index(request):

    books = Book.objects.all()
    return render(request,"book_outlet/index.html",{
        'books' : books 
    })

def book_details(request,slug):
    # try:    
    #     book = Book.objects.get(slug= slug)
    # except:
    #      raise Http404()
    #this code replaces above code---->
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_details.html',{
        'title':book.title,
        'author':book.author,
        'rating':book.rating,
        'is_bestseller': book.is_bestselling,
        'slug':book.slug
    }) 