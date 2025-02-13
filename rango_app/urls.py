from django.urls import path
from rango_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page_id>/', views.detail, name='detail'),
    path('<int:category_id>/results/', views.results, name='results'),
    path('<int:page_id>/vote/', views.vote, name='vote'),
    path('add_category/', views.add_category, name='add_category'),

]
