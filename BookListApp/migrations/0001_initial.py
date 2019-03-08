# Generated by Django 2.1.7 on 2019-03-08 07:23

import BookListApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=100)),
                ('date_published', models.DateField()),
                ('number_of_pages', models.IntegerField()),
                ('type_of_book', models.CharField(choices=[(BookListApp.models.BookType('Novel'), 'Novel'), (BookListApp.models.BookType('Documentation'), 'Documentation'), (BookListApp.models.BookType('Other'), 'Other')], max_length=5)),
            ],
        ),
    ]
