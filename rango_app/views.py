from django.shortcuts import render, get_object_or_404
from rango_app.models import Category, Page
from rango_app.forms import CategoryForm, PageForm
from django.core.cache import cache
# Create your views here.
def index(request):
    categories = cache.get('all_categories')
    if not categories:
        categories = Category.objects.all()
        cache.set('all_categories', categories, timeout=60*15)

    pages = Page.objects.select_related('category').prefetch_related('category').all()
    return render(request, 'index.html', {'categories': categories, 'pages': pages})

def detail(request, page_id):
    page = Page.objects.select_related('category').get(id=page_id)
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

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'category_detail.html', {'category': category})

def page_detail(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'page_detail.html', {'page': page})