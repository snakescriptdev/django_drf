from django.contrib import admin
from .models import Category, Tags, BlogPost
# Register your models here.
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(BlogPost)
