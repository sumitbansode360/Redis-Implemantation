from django.core.cache import cache
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book, Category
from rest_framework.generics import ListAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .tasks import send_email_task, send_email_task_e

# Create your views here.
@api_view(['GET'])
def get_books(request):
    redis_key = "cache:books"

    try:
        data = cache.get(redis_key)
    except Exception:
        data = None
    
    if data:
        print("cache hit!")
        return Response(data)

    books = Book.objects.all().select_related('category')
    serializer = BookSerializer(books, many=True)
    all_books = serializer.data
    print("from db")

    try:
        cache.set(redis_key, all_books, timeout=300)
    except Exception:
        pass

    return Response(all_books)

class BookListView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):

        cache_key = "cache:books"

        try:
            cache_data = cache.get(cache_key)
        except Exception:
            cache_data = None
        
        if cache_data:
            print("form the cache...")
            return cache_data
        
        books = Book.objects.all().select_related('category')
        print("form the db...")
        
        try:
            cache.set(cache_key, books, timeout=300)
        except Exception:
            pass

        return books

@method_decorator(cache_page(60 * 5), name="dispatch")
class BookList(ListAPIView):
    queryset = Book.objects.all().select_related('category')
    serializer_class = BookSerializer

@api_view(['POST'])
def send_email(request):
    email = request.data.get('email')
    send_email_task.delay(email)
    return Response({"message": "Email sent!"})

@api_view(['POST'])
def send_email_e(request):
    email = request.data.get('email')
    send_email_task_e.delay(email)
    return Response({"message": "Email sent!"})