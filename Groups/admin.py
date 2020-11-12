from django.contrib import admin
from .models import Group, GroupList, Post

# Register your models here.
admin.site.register(Group)
admin.site.register(GroupList)
admin.site.register(Post)