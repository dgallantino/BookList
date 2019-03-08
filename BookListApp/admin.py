from django.contrib import admin

from BookListApp import models
# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    model = models.Book
    list_display = ['title', 'author', 'date_published', 'type_of_book']
    list_filter = ('author', 'date_published', 'type_of_book')

admin.site.register(models.Book, BooksAdmin)
