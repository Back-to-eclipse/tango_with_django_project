from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def detail(request, page_id):
    return render(request, 'detail.html', {'page_id': page_id})

from django.http import HttpResponse

def results(request, category_id): 
    return HttpResponse(f"You are viewing results for category {category_id}.")

def vote(request, page_id): 
    return HttpResponse(f"You are voting on page {page_id}.")