from django.db import models
from django.contrib.auth.models import User
from books_1.models import Book
from django.conf import settings
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', 
                              upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class LibraryBook(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True)
    in_library = models.BooleanField(default=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)

class Library(models.Model):      
    user = models.OneToOneField(User,
                             on_delete=models.CASCADE)
    library_book = models.ManyToManyField(LibraryBook)
    
    def __str__(self):
        return f'{self.user.username} Library'