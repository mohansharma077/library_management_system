# library/serializers.py
from rest_framework import serializers
from .models import User, Book, BookDetails, BorrowedBooks
from rest_framework import serializers
from .models import BookDetails
from rest_framework import serializers
from .models import BorrowedBooks

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['UserID', 'Name', 'Email', 'MembershipDate']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['BookID', 'Title', 'ISBN', 'PublishedDate', 'Genre']



class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetails
        fields = '__all__'


class BorrowedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields = '__all__'
