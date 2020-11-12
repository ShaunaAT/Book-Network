"""book_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from pages.views import home_view, about_view
from books_1.views import book_detail_view, book_create_view
from users.views import register, profile, library_view, search_view, \
                        BookDetailView
from Groups.views import group_options_view, create_group_view, join_group_view, \
                        group_view, CreatePostView, PostDetailView, PostDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', book_detail_view),
    path('create/', book_create_view),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout'),
    path('home/', include("pages.urls"), name = 'home'),
    path('', home_view),
    path('groupoptions/', group_options_view),
    path('joingroup/', join_group_view, name = 'join_group'),
    path('creategroup/', create_group_view, name = 'create_group'),
    path('register/', register, name = "register"),
    path('profile/', profile, name = "profile"),
    path('about/', about_view, name = "about"),
    path('library/', library_view, name = "library"),
    path('search/', search_view, name = "search"),
    path('book/<int:pk>/', BookDetailView.as_view(), name = "book-detail"),
    path('group/<int:pk>/', group_view.as_view(template_name='Groups/group.html'), name = "group"),
    path('group/<int:pk>/create_post/', CreatePostView.as_view(), name = "create_post"),
    path('post/<int:pk>/', PostDetailView.as_view(), name = "post-detail"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = "post-delete")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)