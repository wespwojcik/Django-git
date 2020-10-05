from django.shortcuts import render
from django.http import HttpResponse
from .models import Products




def admin_console(request):
    products = Products.objects.all()
    return render(request, 'products/products_page.html', {'products': products})