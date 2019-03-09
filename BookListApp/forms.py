from django import forms
from BookListApp import models

class BookBaseForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'

class BookCreationForm(BookBaseForm):
    """Creation Form"""
    def __init__(self, *args, **kwargs):
        super(BookCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
            visible.field.widget.attrs['required'] = True
    class Media:
        css = {
            'all':(
                'BookListApp/css/add-form.css',
            )
        }

        js = (
            'BookListApp/js/add-form.js',
        )


class BookUpdateForm(BookBaseForm):
    """Update Form"""
