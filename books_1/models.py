from django.db import models


class Book(models.Model):
    title = models.CharField(max_length = 120) 
    author = models.CharField(max_length = 50)
    image_url = models.URLField(default = None)
    book_id = models.CharField(max_length = 25, default = None)
    note = models.CharField(blank = True, max_length = 200)
    

