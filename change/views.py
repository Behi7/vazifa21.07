from django.shortcuts import render
from .models import ProductDay
from django.views.generic import CreateView, UpdateView, DeleteView


class ProductDayCreateView(CreateView):
    model = ProductDay
    template_name = 'product_day/create.html'
    fields = ['name', 'category', 'status', 'img', 'price']

class ProductDayUpdateView(UpdateView):
    model = ProductDay
    template_name = 'product_day/update.html'
    fields = ['name', 'category', 'status', 'img', 'price']

class ProductDayDeleteView(DeleteView):
    model = ProductDay
    template_name = 'product_day/delete.html'
    success_url = '/'
