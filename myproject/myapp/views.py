from django.shortcuts import render, redirect
from myapp.models import *

def products(request):
    all_products = Products.objects.all()
    return render(request, "home.html", {"records" : all_products})
