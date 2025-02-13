from django.shortcuts import render
from rango_app.models import Category, Page


# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def detail(request, page_id):
    page = Page.objects.get(id=page_id)
    return render(request, 'detail.html', {'page': page})

from django.http import HttpResponse

def results(request, category_id): 
    return HttpResponse(f"You are viewing results for category {category_id}.")

def vote(request, page_id): 
    return HttpResponse(f"You are voting on page {page_id}.")