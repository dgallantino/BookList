# Generated by Django 2.1.7 on 2019-03-08 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookListApp', '0003_auto_20190308_0749'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
