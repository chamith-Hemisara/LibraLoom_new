# Generated by Django 4.2.5 on 2023-11-11 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraLoom', '0009_alter_reservation_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(blank=True, null=True, upload_to='LibraLoom/static/images/Books'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, upload_to='LibraLoom/static/images/Category'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_image',
            field=models.ImageField(blank=True, null=True, upload_to='LibraLoom/static/images/Members'),
        ),
    ]
