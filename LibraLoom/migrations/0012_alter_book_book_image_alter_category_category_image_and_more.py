# Generated by Django 4.2.5 on 2023-11-11 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraLoom', '0011_alter_book_book_image_alter_category_category_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(blank=True, null=True, upload_to='Books'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, upload_to='category'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_image',
            field=models.ImageField(blank=True, null=True, upload_to='Members'),
        ),
    ]
