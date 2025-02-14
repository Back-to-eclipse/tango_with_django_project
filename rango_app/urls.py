from django.urls import path, include
from rango_app import views

app_name = 'rango_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('categories/', views.categories, name='categories'),
    path('category/<slug:category_name_slug>/', views.category_detail, name='category_detail'),
    path('page/<int:page_id>/', views.page_detail, name='page_detail'),
    path('page/<int:page_id>/vote/', views.vote, name='vote'),
    path('add-category/', views.add_category, name='add_category'),
    path('search/', views.search, name='search')
]

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


