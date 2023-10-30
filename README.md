# DJANGO REST FRAMEWORK - API (DRF-API)
Django Rest Framework - API (DRF) is a Django application that provides a set of API endpoints for Django Rest Framework (DRF) applications.

## Installation
Install DRF using pip:
```bash
pip install djangorestframework
```

### External Dependencies
```bash
pip install markdown     # Markdown support for the browsable API.

pip install django-filter  # Filtering support
```

## Quickstart
1. Add "rest_framework" to your INSTALLED_APPS setting like this:
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

2. Include the DRF-API URLconf in your project urls.py like this:
```python
path('api-auth/', include('rest_framework.urls')),
```

3. Run `python manage.py migrate` to create the DRF-API models.

4. Start the development server and visit http://127.0.0.1:8000


## New Application with drf and models

1. Create a new application
```bash
python manage.py startapp <app_name>
```

2. Add the new application to the INSTALLED_APPS setting like this:
```python
INSTALLED_APPS = [
    ...
    '<app_name>',
]
```

3. Create a new model in the new application
```python
from django.db import models

class <ModelName>(models.Model):
    <field_name> = models.<field_type>(<field_options>)
```
run makemiagration and migrate

4. Create a new serializer in the new application
```python
# serializers.py

from rest_framework import serializers
from .models import <ModelName>

class <ModelName>Serializer(serializers.ModelSerializer):
    class Meta:
        model = <ModelName>
        fields = '__all__'
```

5. Create a new view in the new application
```python
# views.py

from rest_framework import viewsets
from .models import <ModelName>
from .serializers import <ModelName>Serializer

class <ModelName>ViewSet(viewsets.ModelViewSet):
    queryset = <ModelName>.objects.all()
    serializer_class = <ModelName>Serializer
```

6. Add the new view to the urls.py
```python

from django.urls import path, include
from rest_framework import routers
from .views import <ModelName>ViewSet

router = routers.DefaultRouter()
router.register('<model_name>', <ModelName>ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

7. Add the new urls to the project urls.py
```python
from django.urls import path, include

urlpatterns = [
    ...
    path('<app_name>/', include('<app_name>.urls')),
]
```


