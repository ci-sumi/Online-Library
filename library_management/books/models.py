from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.CharField(max_length=20,unique=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    published_date = models.DateField()
    cover_image = models.URLField(default='https://example.com/placeholder-image.jpg')
   
    
    def __str__(self):
        return self.title
     