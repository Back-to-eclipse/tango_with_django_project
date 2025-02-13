import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import django
django.setup()

from rango_app.models import Category, Page

def populate():
    python_pages = [
        {'title': 'Python Official Site', 'url': 'https://www.python.org/', 'views': 100},
        {'title': 'Learn Python', 'url': 'https://www.learnpython.org/', 'views': 75},
    ]

    django_pages = [
        {'title': 'Django Official Site', 'url': 'https://www.djangoproject.com/', 'views': 85},
        {'title': 'Django Docs', 'url': 'https://docs.djangoproject.com/en/2.2/', 'views': 30},
    ]

    cats = {
        'Python': {'pages': python_pages},
        'Django': {'pages': django_pages},
    }

    for cat, cat_data in cats.items():
        c = add_category(cat)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
