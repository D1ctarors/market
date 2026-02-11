from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.db.models import Q

from .models import Category, Size, ProductSize,  Product, ProductImage


def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)[:8]
    return render(request=request, template_name='market_app/home.html', context={
        'categories': categories,
        'products': products,
    })

def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request=request, template_name='market_app/catalog.html', context = {
        'category': category,
        'categories': categories,
        'products': products,
    })


def product_detail(request, id, product_slug):
    product = get_object_or_404(Product, id=id, slug=product_slug, available=True)
    related_products = Product.objects.filter(category=product.category, available=True).exclude(id=product.id)[:5] # Получаем 5 похожих товаров из текущей категории
    return render(request=request, template_name='market_app/detail.html', context={
        'product': product,
        'related_products': related_products,
    })


def cart(request):
    cart_items = Product.objects.filter(available=True)[:3]
    return render(request=request, template_name='market_app/cart.html', context={
        'cart_items': cart_items,
    })


# TODO: Перейти на классовое представление
# class IndexView(TemplateView):
#     template_name = 'market_app/catalog.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all()
#         context['current_category'] = None
#
#         return context
#
#     def get(self, request, *args, **kwargs):
#         context = self.get_context_data(**kwargs)
#
#         if request.headers.get('HX-Request'):
#             return TemplateResponse(request=request, template='market_app/home_content.htmk', context = context)
#
#         return TemplateResponse(request=request, template=self.template_name, context=context)
#
#
# class CatalogView(TemplateView):
#     template_name = 'market_app/catalog.html'
#
#     FILTER_MAPPING = {
#         'color': lambda queryset, value: queryset.filter(color__iexact=value),
#         'min_price': lambda queryset, value: queryset.filter(price_gte=value),
#         'max_price': lambda queryset, value: queryset.filter(price_lte=value),
#         'size': lambda queryset, value: queryset.filter(product_sizes__size__name=value),
#     }
