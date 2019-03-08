from enum import Enum
from django.db import models

# Create your models here.

class BookType(Enum):
    NOV = "Novel"
    DOC = "Documentation"
    OTH = "Other"

class Book(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)

    date_modified = models.DateTimeField(auto_now=True)

    title = models.CharField(
        max_length = 40,
        null = False,
        blank = False,
    )

    author = models.CharField(
        max_length = 100,
        null = False,
        blank = False,
    )

    date_published = models.DateField(null=True,blank=True,)

    number_of_pages = models.IntegerField(null=True,blank=True,)

    NOV = 'NOV'
    DOC = 'DOC'
    OTH = 'OTH'

    type_of_book = models.CharField(
        max_length = 3,
        choices = (
            (NOV, 'Novel'),
            (DOC, 'Documentation'),
            (OTH, 'Other'),
        ),
        null=True,
        blank=True,
    )
