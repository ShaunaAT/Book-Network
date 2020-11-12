from django.contrib import admin

from .models import Profile, Library, LibraryBook

admin.site.register(Profile)

admin.site.register(Library)
admin.site.register(LibraryBook)


