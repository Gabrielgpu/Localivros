from django.urls import path
from .views import *



urlpatterns = [
  path('', BookListView.as_view(), name='books'),
  path('add/', BookCreateView.as_view(), name='add_book'),
  path('<int:id>/', BookDetailView.as_view(), name='book_detail'),
  path('update/<int:id>/', BookUpdateView.as_view(), name='update_book'),
  path('delete/<int:id>/', BookDeleteView.as_view(), name='delete_book')
]