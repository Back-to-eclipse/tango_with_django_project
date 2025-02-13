from django.shortcuts import render
from rango_app.models import Category, Page
from rango_app.forms import CategoryForm, PageForm


# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def detail(request, page_id):
    page = Page.objects.get(id=page_id)
    return render(request, 'detail.html', {'page': page})

def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'add_category.html', {'form': form})

from django.http import HttpResponse

def results(request, category_id): 
    return HttpResponse(f"You are viewing results for category {category_id}.")

def vote(request, page_id): 
    return HttpResponse(f"You are voting on page {page_id}.")