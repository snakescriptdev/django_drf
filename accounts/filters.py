import django_filters
from django_filters.rest_framework import FilterSet

from accounts.models import BlogPost


class BlogPostFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = BlogPost
        fields = ['title', 'category', 'tags']