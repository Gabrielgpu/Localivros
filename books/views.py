from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy   
from django.shortcuts import redirect
from django.db.models import Q
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
  paginate_by = 5
  ordering = ['id']


  def get_queryset(self):
      queryset = super().get_queryset()
      query = self.request.GET.get('query')

      if query:
        search_fields = ['id', 'created_at', 'description', 'gtin_ean', 'product_category', 'author', 'user_id__username', 'year_published']

        query_objects = Q()
        for field in search_fields:
          query_objects |= Q(**{f"{field}__icontains": query})

        queryset = queryset.filter(query_objects)

      return queryset
  

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

  



