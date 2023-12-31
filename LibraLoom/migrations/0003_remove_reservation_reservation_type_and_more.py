# Generated by Django 4.2.5 on 2023-11-04 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraLoom', '0002_book_category_member_reservation_delete_books_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='reservation_type',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_download_link',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(blank=True, null=True, upload_to='book_images/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_pages',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_publisher',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_rating',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_image',
            field=models.ImageField(blank=True, null=True, upload_to='member_images/'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
