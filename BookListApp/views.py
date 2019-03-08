from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


from BookListApp import models
# Create your views here.


class MainListView(ListView):
    template_name = 'BookListApp/mainpage.html'
    context_object_name = 'Books'
    model=models.Book
    def get_context_data(self,**kwargs):
        context = super(MainListView,self).get_context_data(**kwargs)
        context["Navigations"] = ["Home",]
        return context

class DeleteBookView(DeleteView):
    model = models.Book
    succes_url = reverse_lazy('BookListApp:home')
