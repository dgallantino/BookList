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
        #styling using atributes
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
        self.fields.get("date_published").widget.attrs["placeholder"]="Date published (dd/mm/yyyy)"
    class Media:
        css = {
            'all':(
                'BookListApp/css/add-form.css',
                'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.8.0/css/bootstrap-datepicker.css',
            )
        }

        js = (
            'BookListApp/js/add-form.js',
            'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.8.0/js/bootstrap-datepicker.js',
        )


class BookUpdateForm(BookBaseForm):
    """Update Form"""
