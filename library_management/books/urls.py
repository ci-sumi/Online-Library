from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('books/',views.index,name='index'),
    path('books/all/',views.all_book_view,name='all_book_view')

]
