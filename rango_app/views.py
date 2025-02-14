from django.shortcuts import render, get_object_or_404,redirect
from rango_app.models import Category, Page
from rango_app.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.core.cache import cache
from django.http import JsonResponse
import requests
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
            form.save()
            return redirect('rango_app:index')
    return render(request, 'add_category.html', {'form': form})

from rango_app.forms import UserForm, UserProfileForm
from django.shortcuts import render

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rango_app/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

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

def show_category(request, category_name_slug):
    category = get_object_or_404(Category, slug=category_name_slug)
    pages = Page.objects.filter(category=category)

    category.views = category.views + 1
    category.save()

    context_dict = {'category': category, 'pages': pages}
    return render(request, 'rango_app/category.html', context=context_dict)

def like_page(request):
    page_id = request.GET.get('page_id')
    try:
        page = Page.objects.get(id=int(page_id))
        page.likes += 1
        page.save()
        return JsonResponse({'likes': page.likes})
    except Page.DoesNotExist:
        return JsonResponse({'error': 'Page not found'})
    
def bing_search(query):
    endpoint = 'https://api.bing.microsoft.com/v7.0/search'
    headers = {'Ocp-Apim-Subscription-Key': settings.BING_API_KEY}
    params = {'q': query, 'textDecorations': True, 'textFormat': 'HTML'}
    response = requests.get(endpoint, headers=headers, params=params)
    return response.json()

def search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = bing_search(query).get('webPages', {}).get('value', [])
    return render(request, 'rango_app/search.html', {'query': query, 'results': results})