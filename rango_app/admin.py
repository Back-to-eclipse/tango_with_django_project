from django.contrib import admin

# Register your models here.
from rango_app.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'views')
    list_filter = ('category',)
    search_fields = ('title', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name': ('name',)}
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)