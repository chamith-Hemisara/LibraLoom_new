from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category_image = models.ImageField(upload_to='category_images/', blank=True)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Add other fields like ISBN, publication date, etc.
    book_id = models.CharField(max_length=100)
    book_image = models.ImageField(upload_to='book_images/', blank=True)
    book_download_link = models.CharField(max_length=100)
    book_description = models.TextField()
    ISBN = models.CharField(max_length=100)
    publication_date = models.DateField()
    book_status = models.CharField(max_length=100)
    book_rating = models.CharField(max_length=100)
    book_publisher = models.CharField(max_length=100)
    book_pages = models.CharField(max_length=100)
    book_language = models.CharField(max_length=100)


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Assuming you have a User model for authentication
    # Add additional member-related fields like address, phone number, etc.
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    member_image = models.ImageField(upload_to='member_images/', blank=True)
    member_id = models.CharField(max_length=100)
    member_status = models.CharField(max_length=100)
    member_type = models.CharField(max_length=100)
    member_dob = models.DateField()


class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)
    # Add additional fields for managing reservations, like due date, status, etc.
    due_date = models.DateField()
    status = models.CharField(max_length=100)
    reservation_id = models.CharField(max_length=100)
    reservation_type = models.CharField(max_length=100)
    reservation_status = models.CharField(max_length=100)
    reservation_date = models.DateField()
