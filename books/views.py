from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy   
from django.shortcuts import redirect
from .models import Book
from .forms import EditBookForm



class BookCreateView(LoginRequiredMixin, CreateView):
  model = Book
  template_name = 'register_book.html'
  success_url = reverse_lazy('book_search')
  success_message = 'Livro cadastrado com sucesso!'
  error_message = 'Dados insuficientes para cadastrar o livro.'

  def post(self, request, *args, **kwargs):
    metadata = request.session.pop('book_metadata', None)
    stock = request.POST.get('stock')

    if metadata and stock:
      Book.objects.create(
        description = metadata.get('title', ''),
        price = metadata.get('price', ''),
        gtin_ean = metadata.get('gtin_ean', ''),
        width = metadata.get('height', ''),
        height = metadata.get('width', ''),
        depth = metadata.get('depth', ''),
        mark = metadata.get('editora', ''),
        short_description = metadata.get('short_description', ''),
        url_external_images = metadata.get('url_external_images', ''),
        product_category = metadata.get('product_category', ''),
        additional_information = metadata.get('mark', ''),
        year_published = metadata.get('year_published', ''),
        page_of_number = metadata.get('page_of_number', ''),
        author = metadata.get('author', ''),
        stock = stock
      )
      messages.success(request, self.success_message)
    else:
      messages.error(request, self.error_message)

    return redirect(self.success_url)

class BookListView(LoginRequiredMixin, ListView):
  model = Book
  template_name = 'books.html'
  context_object_name = 'products'

class BookDetailView(LoginRequiredMixin, DetailView):
  model = Book
  template_name = 'detail_book.html'
  pk_url_kwarg = 'id'
  context_object_name = 'product'

class BookUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  form_class = EditBookForm
  model = Book
  pk_url_kwarg = 'id'
  template_name = 'update_book.html'
  success_url = reverse_lazy('books')
  success_message = 'Livro atualizado!'

class BookDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
  pk_url_kwarg = 'id'
  model = Book
  success_url = reverse_lazy('books')
  success_message = 'Livro removido!'

  



