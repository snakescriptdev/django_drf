# View and Viewset
- Viewset is a class that provides the functionality of a view. It handles the http request and response.
- View is a function that takes a request and returns a response. It can be class based or function based.

## Function-based views vs. class-based views
- Function-based views are the most simple views, and are generally used for one of two purposes:
    - The view itself is a callback function for a particular URL, because it’s the simplest way to write a view.
    - You need the (slight) performance overhead of the basic view to be as low as possible.

- Class-based viws are the most powerful and customizable views. They are used for:
    - Reuse of common logic between views.
    - Wrapping the view in another function.
    - Creating a subclass of the view to alter its behavior.

### Example of Function-based view
```python
from django.http import HttpResponse
from django.shortcuts import render

def my_view(request):
    if request.method == 'GET':
        return HttpResponse('result')
    elif request.method == 'POST':
        return HttpResponse('result')
    elif request.method == 'PUT':
        return HttpResponse('result')
    elif request.method == 'DELETE':
        return HttpResponse('result')
```

### Example of Class-based view
```python
from django.http import HttpResponse
from django.views import View

class ApiView(View):
  def get(self, request):
    return HttpResponse('result')
  def post(self, request):
    return HttpResponse('result')

```