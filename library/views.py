from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Book, BorrowedBooks, BookDetails
from .serializers import UserSerializer, BookSerializer, BookDetailsSerializer, BorrowedBooksSerializer
from .forms import CreateUserForm, AddBookForm, BorrowBookForm  # Import the forms
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import BorrowBookForm, ReturnBookForm
from .models import BorrowedBooks
from .serializers import BorrowedBooksSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, BookDetails
from .serializers import BookSerializer, BookDetailsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Book, BorrowedBooks
from .serializers import UserSerializer, BookSerializer, BorrowedBooksSerializer
from .forms import BorrowBookForm, ReturnBookForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BorrowedBooks
from .forms import BorrowBookForm
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import BorrowBookForm
from .models import BorrowedBooks
from .serializers import BorrowedBooksSerializer



@api_view(['GET','POST'])
def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.data)
        if form.is_valid():
            user = form.save()
            serializer = UserSerializer(user)
            return Response(serializer.data, status=201)
    else:
        form = CreateUserForm()

    return render(request, 'create_user.html', {'form': form})

@api_view(['GET','POST'])
def add_new_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.data)
        if form.is_valid():
            book = form.save()
            serializer = BookSerializer(book)
            return Response(serializer.data, status=201)
    else:
        form = AddBookForm()

    return render(request, 'add_new_book.html', {'form': form})




@api_view(['GET'])
def list_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_user_by_id(request, user_id):
    user = User.objects.get(UserID=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)




@api_view(['GET'])
def list_all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_book_by_id(request, book_id):
    book = Book.objects.get(BookID=book_id)
    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT'])
def assign_update_book_details(request, book_id):
    try:
        book = Book.objects.get(BookID=book_id)
    except Book.DoesNotExist:
        return Response({"message": "Book not found"}, status=404)

    if request.method == 'POST':
        # Create new book details
        serializer = BookDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(book=book)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        # Update existing book details
        try:
            book_details = BookDetails.objects.get(book=book)
        except BookDetails.DoesNotExist:
            return Response({"message": "Book details not found"}, status=404)

        serializer = BookDetailsSerializer(book_details, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'GET':
        # Retrieve existing book details
        serializer = BookDetailsSerializer(book.bookdetails)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def borrow_book(request):
    if request.method == 'POST':
        form = BorrowBookForm(request.data)
        if form.is_valid():
            form.save()
            return Response({"message": "Book borrowed successfully"}, status=201)
        return Response(form.errors, status=400)
    elif request.method == 'GET':
        borrowed_books = BorrowedBooks.objects.all()
        serializer = BorrowedBooksSerializer(borrowed_books, many=True)
        return Response(serializer.data)
    return Response({"message": "Method not allowed"}, status=405)






@api_view(['POST'])
def return_book(request, borrowed_book_id):
    try:
        borrowed_book = BorrowedBooks.objects.get(id=borrowed_book_id)
    except BorrowedBooks.DoesNotExist:
        return Response({"message": "Borrowed book not found"}, status=404)

    if request.method == 'POST':
        form = ReturnBookForm(request.data, instance=borrowed_book)
        if form.is_valid():
            form.save()
            return Response({"message": "Book returned successfully"}, status=200)
        return Response(form.errors, status=400)

    return Response({"message": "Method not allowed"}, status=405)


@api_view(['GET'])
def list_borrowed_books(request):
    borrowed_books = BorrowedBooks.objects.all()
    serializer = BorrowedBooksSerializer(borrowed_books, many=True)
    return Response(serializer.data)
