from django.urls import path
from .views import *


urlpatterns = [
    path('', ScrapingView.as_view(), name='book_search')
]
