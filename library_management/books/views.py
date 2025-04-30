import requests
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Book
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    print("Index view is being called!")
    return render(request,'index.html')

# def get_books():
#     books = []
#     api_url = "https://www.gutenberg.org/ebooks/1342"
#     response = request.get(api_url)
#     if response.status_code== 200:
#         data = response.json()
#         books = data.get('docs',[])[:10]
#     return books

# fetchbook = get_books()
def get_bookapi(query='Malayalam classic novel', max_book= 40):
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_book}'
    response = requests.get(url)
    books=[]
    
    if response.status_code==200:
        data  =  response.json()
        items = data.get('items',[])
        for book in items:
            volume_info = book.get('volumeInfo',{})
            books.append({
                'title': volume_info.get('title', 'Unknown'),
                'authors': ', '.join(volume_info.get('authors', ['Unknown'])),
                'published_date': volume_info.get('publishedDate', 'N/A'),
                'book_id': book.get('id'),
                'categories': ', '.join(volume_info.get('categories', ['No Category'])),
                'image_url':volume_info.get('imageLinks',{}).get('thumbnail','No image')
            })
            
    return books



# to save the data to the database
def save_to_database(request):
    books = get_bookapi()
    print(books)
    if not books:
        return HttpResponse ("No books returned from API")
    for books_data in books:
                
        Book.objects.update_or_create(
        book_id = books_data['book_id'],
        defaults={
            'title':books_data['title'],
            'author':books_data['authors'],
            'subject':books_data['categories'],
            'published_date':get_published_year(books_data.get('published_date')),
            'cover_image':books_data['image_url'],
            
        }
     )
    return HttpResponse (f"successfully saved {len(books)} books to the database")

    

 
def all_book_view(request):
    books = get_bookapi()
    return render(request,'allbook.html',{'books':books})