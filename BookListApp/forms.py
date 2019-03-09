from django import forms
from BookList import settings
from BookListApp import models

class BookBaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookBaseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
    class Meta:
        model = models.Book
        fields = '__all__'

class BookCreationForm(BookBaseForm):
    """Creation Form"""
    def __init__(self, *args, **kwargs):
        super(BookCreationForm, self).__init__(*args, **kwargs)
        self.fields.get("date_published").widget.attrs["placeholder"]="Date published (dd MM, yyyy)"
    class Meta(BookBaseForm.Meta):
        widgets = {
            'date_published':forms.DateInput(format="%d %B, %Y"),
        }
    class Media:
        css = {
            'all':(
                'BookListApp/css/book-add.css',
                'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.8.0/css/bootstrap-datepicker.css',
            )
        }

        js = (
            'BookListApp/js/book-add.js',
            'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.8.0/js/bootstrap-datepicker.js',
        )


class BookUpdateForm(BookBaseForm):
    """Update Form"""
    class Meta(BookBaseForm.Meta):
        widgets = {
            'date_published':forms.DateInput(format="%d %B, %Y"),
        }
    class Media:
        css = {
            'all':(
                'BookListApp/css/book-update.css',
                'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.8.0/css/bootstrap-datepicker.css',
            )
        }

        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.8.0/js/bootstrap-datepicker.js',
        )
