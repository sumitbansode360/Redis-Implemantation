from .models import Product
from django.core.cache import cache
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_product(request):
    cache_key = "cache:products"

    try:
        data = cache.get(cache_key)
    except Exception as e:
        data = None
    
    if data:
        print("fetching from cache...")
        return Response(data)
    
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    print("fetching from db...")
    try:
        cache.set(cache_key, serializer.data, 300)
    except Exception:
        pass

    return Response(serializer.data)

    
@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete("cache:products")
        print("cache deleted")
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
