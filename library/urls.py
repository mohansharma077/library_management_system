# library/urls.py
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *


app_name = 'library'
urlpatterns = [
    # User APIs
    path('users/create/', create_user, name='create_user'),
    path('users/list/', list_all_users, name='list_all_users'),
    path('users/<int:user_id>/', get_user_by_id, name='get_user_by_id'),

    # Book APIs
    path('books/add/', add_new_book, name='add_new_book'),
    path('books/list/', list_all_books, name='list_all_books'),
    path('books/<int:book_id>/', get_book_by_id, name='get_book_by_id'),
    path('books/<int:book_id>/details/', assign_update_book_details, name='assign_update_book_details'),

    # BorrowedBooks APIs
    path('borrow/', borrow_book, name='borrow_book'),
    path('return/', return_book, name='return_book'),
    path('list-borrowed/', list_borrowed_books, name='list_borrowed_books'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)