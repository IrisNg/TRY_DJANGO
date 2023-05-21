"""
URL configuration for movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from movies import views # movies -> folder name, views -> views.py file

# Checkout namespace for urls if multiple apps share the same name
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', views.movies), # views.movies -> 'movies' function in views.py
    path('movies/home', views.home),
    path('movies/<int:id>', views.movie_detail, name='detail'),
    path('movies/create', views.create_movie, name='create'),
    path('movies/list', views.movie_list)
]
