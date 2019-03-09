from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages


from BookListApp import models, forms
# Create your views here.


class MainListView(CreateView):
    template_name = 'BookListApp/main-page.html'
    model=models.Book
    form_class = forms.BookCreationForm
    success_url = reverse_lazy('BookListApp:home')

    def get_context_data(self,**kwargs):
        context = super(MainListView,self).get_context_data(**kwargs)
        #context for the book list
        context["Books"] = self.model.objects.all();
        #context for navigation
        context["Navigations"] = ["Home",]
        return context

    def form_invalid(self, form):
        html_message=""

        for idx, field_messages in form.errors.items():
            for message in field_messages:
                html_message = html_message + message +"\n"

        messages.add_message(
            request=self.request,
            level=messages.ERROR,
            message=html_message,
            fail_silently=True,
        )
        
        return super(MainListView, self).form_invalid(form);

class DeleteBookView(DeleteView):
    model = models.Book
    success_url = reverse_lazy('BookListApp:home')

class UpdateBookView(UpdateView):
    model = models.Book
    success_url = reverse_lazy('BookListApp:home')
