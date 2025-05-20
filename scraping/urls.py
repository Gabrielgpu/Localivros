from django.urls import path
from .views import *


urlpatterns = [
    path('buscar/', BookSearch, name='book_search')
]
