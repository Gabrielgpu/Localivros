from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView



class BookCreateView(CreateView):
  pass

class BookListView(ListView):
  pass

class BookDetailView(DetailView):
  pass

class BookUpdateView(UpdateView):
  pass

class BookDeleteView(DeleteView):
  pass



