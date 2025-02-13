from django.contrib import admin
from django.urls import path
from rango_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('page/<int:page_id>/', views.page_detail, name='page_detail'),
    path('page/<int:page_id>/vote/', views.vote, name='vote'),
    path('add-category/', views.add_category, name='add_category'),
    path('admin/', admin.site.urls),
]
