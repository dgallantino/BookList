from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy


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

class DeleteBookView(DeleteView):
    model = models.Book
    success_url = reverse_lazy('BookListApp:home')

class UpdateBookView(UpdateView):
    model = models.Book
    success_url = reverse_lazy('BookListApp:home')
