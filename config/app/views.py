from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BookListView(ListView):
    model = models.Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookCreateView(CreateView):
    model = models.Book
    fields = '__all__'
    template_name = 'book_form.html'
    success_url = reverse_lazy('index')

class BookUpdateView(UpdateView):
    model = models.Book
    fields = '__all__'
    template_name = 'book_form.html'
    success_url = reverse_lazy('index')

class BookDeleteView(DeleteView):
    model = models.Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('index')

