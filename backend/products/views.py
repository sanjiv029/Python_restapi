from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
        
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance = serializer.save()
              
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
    
       
    
    
    #lookup_field = 'pk'
    #product.object.get(pk=1)
    
# @api_view(["GET", "POST"])   
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method 
     
#     if method == "GET":
#         if pk is not None:
#             #detail_view
#             obj = get_object_or_404(Product,pk=pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)
#         #list view
#         queryset = Product.objects.all()
#         data = ProductSerializer(queryset,many=True).data
#         return Response(data)
    
#     if method == "POST":
#         #create view
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)
#         return Response(serializer.errors,status=400)    