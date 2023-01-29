import json
from django.http import JsonResponse

from products.models import Product


def api_home(request, *args, **kwargs):
    model_data = Products.objects.all().order_by("?").first()
    """
    # request.body -> HttpRequest from Django
    body = request.body #byte string of JSon Data
    data ={}
    try: 
        data = json.loads(body) # string of JSON data -> Python Dict
    except:
        pass    
    print(data)
    #data['headers'] = request.headers
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type 
    """
    return JsonResponse(data)
 