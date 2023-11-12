from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category_image = models.ImageField(upload_to='category', blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='name')
    # Add other fields like ISBN, publication date, etc.
    book_id = models.CharField(max_length=100)
    book_image = models.ImageField(upload_to='Books', blank=True, null=True)
    book_download_link = models.CharField(max_length=100,null=True,blank=True)
    book_description = models.TextField()
    ISBN = models.CharField(max_length=100)
    publication_date = models.DateField(null=True,blank=True)
    book_Availability = models.BooleanField(default=True)
    book_rating = models.CharField(max_length=100,null=True,blank=True)
    book_publisher = models.CharField(max_length=100,null=True, blank=True)
    book_pages = models.CharField(max_length=100,null=True, blank=True)
    book_language = models.CharField(max_length=100)


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional member-related fields like address, phone number, etc.
    address = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100)
    member_image = models.ImageField(upload_to='Members', blank=True, null=True)
    member_id = models.CharField(max_length=100)
    member_status = models.CharField(max_length=100)
    member_type = models.CharField(max_length=100, null=True, blank=True)
    member_dob = models.DateField()

    def __str__(self):
        return self.user.username  # Or any other field to represent the member


class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)
    # Add additional fields for managing reservations, like due date, status, etc.
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    reservation_id = models.CharField(max_length=100,null=True, blank=True)
    reservation_status = models.CharField(max_length=100, null=True, blank=True)
    reservation_date = models.DateField(null=True, blank=True)



