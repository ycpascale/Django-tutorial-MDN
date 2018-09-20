from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.index, name='index'),     #Index page catalog/      , catalog/ already taken in locallibrary urls.py file therefore no string
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]