from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from .utils.scraping import ScraperManager
import asyncio
from books.models import Book

scraper = ScraperManager()

class ScrapingView(LoginRequiredMixin, View):
  template_name = 'home.html'
  error_message = 'Isbn é obrigatório!'


  def get(self, request):
    latest_books = Book.objects.order_by('-created_at')[:5]
    return render(request, self.template_name, {'books': latest_books})

  def post(self, request):
    isbn = request.POST.get('isbn')
    metadata_database = Book.objects.filter(gtin_ean=isbn).first()

    if not isbn:
      messages.error(request, self.error_message)
      return redirect('book_search')
    
    if metadata_database:
      messages.info(request, f'O livro "{metadata_database.description}" já está cadastrado.')
      return redirect('book_detail', metadata_database.id)
    
    metadata_scraping = asyncio.run(self.scraping(isbn))

    if metadata_scraping:
      request.session['book_metadata'] = metadata_scraping
      return render(request, 'register_book.html', { 'metadata': metadata_scraping })

    messages.error(request, f'Não foi possível localizar o livro vinculado ao isbn: {isbn}')
    return redirect('book_search')

  async def scraping(self, isbn=None):
    await scraper.start_first_part()

    metadata = await scraper.start_second_part(isbn)

    await scraper.close()

    return metadata