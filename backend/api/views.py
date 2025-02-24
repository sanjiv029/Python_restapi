from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        data = serializer.data
        return Response(data)
    return Response(serializer.errors,status=400)
    # data = request.data
    # instance = Product.objects.all().order_by("?").first()
    # data={}
    # if instance:
    #DRF API View
    # #request -> HTTP request->Django
    # #requests.body
    # body = request.body #byte string
    # data = {}
    # try:
    #     data = json.loads(body) #takes string of data
    # except:
    #     pass
    
    # print(data)
    # data['params']  = dict(request.GET)
    # data['headers'] = dict(request.headers) 
    # print(request.headers)
    # data['content_type'] = request.content_type
    # return JsonResponse(data)    
    #    model_data = model_to_dict(model_data,fields=['id','title','price','sale_price'])
        #serialization
        #model instance (model_data)
        #turn a python dict
        #return JSON data