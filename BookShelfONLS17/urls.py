"""
URL configuration for BookShelfONLS17 project.

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

from django.urls import path
from bookshelf import views


urlpatterns = [
    path('', views.index, name='index'),
    path('szablon/', views.index_z_szablonem, name='index_z_szablonem'),
    path('losuj/', views.losuj, name='losuj'),
    path('losuj_liczby/<int:ilosc>/', views.losuj_6, name='losuj_6'),
    path('nazwisko/<int:index>/', views.get_name, name='nazwiska'),
    path('add_nazwisko/<str:name>/', views.add_name_by_url, name='add_name_by_url'),
    path("add_last_name/", views.add_name, name='add_name2'),
    path("add_author/", views.add_author, name='add_author'),
    path("authors/", views.authors, name='authors'),
    path("update_author/<int:id>/", views.update_author, name='authors'),
    path('create_publisher/', views.create_publisher, name='create_publisher'),
    path('publishers/', views.publishers, name='publishers'),
    path('update_publisher/<int:id>/', views.update_publisher, name='update_publisher'),
    path('delete_publisher/<int:id>/', views.delete_publisher, name='delete_publisher'),

]
