from django.urls import path
from rango_app import views

urlpatterns = [
    path('', views.index, name='index'),
]
