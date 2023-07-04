from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Product, News


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Распродажа в среду!"
        return context

class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class NewsList(ListView):
    model = News
    ordering = 'name'
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()

        return context

class NewsDetail(DetailView):
    model = News
    template_name = 'news_number.html'
    context_object_name = 'news_number'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()

        return context