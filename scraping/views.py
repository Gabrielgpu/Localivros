from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from .utils import ScraperManager
import asyncio
from books.models import Book

scraper = ScraperManager()

class ScrapingView(LoginRequiredMixin, View):
  template_name = 'home.html'
  error_message = 'Isbn é obrigatório!'

  def get(self, request):
    return render(request, self.template_name)

  def post(self, request):
    isbn = request.POST.get('isbn')
    metadata = Book.objects.filter(gtin_ean=isbn).first()

    if not isbn:
      messages.error(request, self.error_message)
      return redirect('book_search')
    
    if not metadata:
      metadata = asyncio.run(self.scraping(isbn))

      request.session['book_metadata'] = metadata

      return render(request, 'register_book.html', { 'metadata': metadata })

    return redirect('book_detail', metadata.id)

  async def scraping(self, isbn=None):
    await scraper.start_first_part()

    metadata = await scraper.start_second_part(isbn)

    await scraper.close()

    return metadata