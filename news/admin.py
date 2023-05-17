from django.contrib import admin

from news.models import Category, FlashNews

# Register your models here.

admin.site.register(Category)
admin.site.register(FlashNews)
