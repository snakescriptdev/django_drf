# DjangoDRF Documentation
In django drf documentation, we will learn how to create a rest api

## Installation
```bash
pip install drf-yasg
```

## Usage
```python
INSTALLED_APPS = [
    ...
    'drf_yasg',
    ...
]
```

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="DjangoDRF API",
        default_version='v1',
        description="DjangoDRF API Documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="vijaysharma@snakescript.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   ...
]
```


https://drf-yasg.readthedocs.io/en/stable/index.html

