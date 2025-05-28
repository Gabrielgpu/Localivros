from django.urls import path
from .views import *


urlpatterns = [
    path('buscar/', ScrapingView.as_view(), name='book_search')
]
