# library/forms.py
from django import forms
from .models import User, Book, BorrowedBooks

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Name', 'Email', 'MembershipDate']
        widgets = {
            'MembershipDate': forms.DateInput(attrs={'type': 'date'}),
        }

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['Title', 'ISBN', 'PublishedDate', 'Genre']
        widgets = {
            'PublishedDate': forms.DateInput(attrs={'type': 'date'}),
        }
# library/forms.py
# library/forms.py
from django import forms
from .models import BorrowedBooks

class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = BorrowedBooks
        fields = ['UserID', 'BookID']

class ReturnBookForm(forms.ModelForm):
    class Meta:
        model = BorrowedBooks
        fields = ['ReturnDate']
