from django.urls import re_path as url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delivery', views.delivery, name='delivery'),
    path('contacts', views.contacts, name='contacts'),
    url(r'^section/(?P<id>\d+)$', views.section, name='section'),
    url(r'^product/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product')

]
