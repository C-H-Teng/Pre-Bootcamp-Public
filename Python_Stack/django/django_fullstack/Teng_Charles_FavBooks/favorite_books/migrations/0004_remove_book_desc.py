# Generated by Django 3.2 on 2021-04-22 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_books', '0003_book_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='desc',
        ),
    ]
