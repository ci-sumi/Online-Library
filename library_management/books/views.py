import requests
from django.shortcuts import render,redirect
from .models import Book

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

# to save the 
 
def all_book_view(request):
    books = get_bookapi()
    return render(request,'allbook.html',{'books':books})