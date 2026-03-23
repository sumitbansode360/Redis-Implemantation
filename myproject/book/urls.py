from django.urls import path
from .views import get_books, BookListView, BookList, send_email

urlpatterns = [
    path('all/', get_books, name='get_book'),
    path('list/', BookListView.as_view(), name="book_list"),
    path('book-list/', BookList.as_view(), name="book_list"),
    # path('create/', create_product, name='create_product')
    path('send-email/', send_email, name='send_email')
]
