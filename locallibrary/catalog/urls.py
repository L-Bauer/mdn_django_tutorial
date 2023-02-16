from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# Books urls
urlpatterns += [
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]

# Author urls
urlpatterns += [
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]