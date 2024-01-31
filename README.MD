# Library Management System

This is a Django-based Library Management System that allows users to manage books, users, and book borrowings.

## Features

- User management: Add, view, and retrieve user details.
- Book management: Add, view, and retrieve book details.
- Borrow and return books: Record borrowings and returns of books by linking users with books.
- List all borrowed books: View a list of all books currently borrowed from the library.

## Setup

1. Clone the repository:

   ```bash
   gh repo clone mohansharma077/library_management_system
   
   OR 
   git@github.com:mohansharma077/library_management_system.git
   cd library-management-system

2.pip install -r requirements.txt


3. python manage.py makemigrations
python manage.py migrate


4. python manage.py createsuperuser


5. python manage.py runserver
