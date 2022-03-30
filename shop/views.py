from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from shop.models import Section, Product


def index(request):
    sections = Section.objects.all().order_by('title')
    products = Product.objects.all().order_by(get_order_by_products(request))[:8]
    context = {'sections': sections, 'products': products}
    return render(
        request,
        'index.html',
        context=context
    )


def get_order_by_products(request):
    order_by = ''
    if request.GET.__contains__('sort') and request.GET.__contains__('up'):
        sort = request.GET['sort']
        up = request.GET['up']
        if sort == 'price' or sort == 'title':
            if up == '0':
                order_by = '-'
            order_by += sort
    if not order_by:
        order_by = '-data'
    return order_by


def delivery(request):
    sections = Section.objects.all().order_by('title')
    return render(
        request,
        'delivery.html',
        context={'sections': sections}
    )


def section(request, id):
    obj = get_object_or_404(Section, pk=id)
    products = Product.objects.filter(section__exact=obj).order_by(get_order_by_products(request))
    context = {'section': obj, 'products': products}
    return render(
        request,
        'section.html',
        context=context
    )


def contacts(request):
    sections = Section.objects.all().order_by('title')
    return render(
        request,
        'contacts.html',
        context={'sections': sections}
    )


class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.filter(section__exact=self.get_object().section)
        return context


def handler404(request, exception):
    return render(request, '404.html', status=404)
