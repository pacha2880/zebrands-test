import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    return HttpResponse('Home page')


def products(request):
    if request.method == 'GET':
        try:
            products = Product.objects.all()
            response = [product.as_json() for product in products]
        except:
            response = 'Error'
    return HttpResponse(json.dumps(response), content_type='application/json')
