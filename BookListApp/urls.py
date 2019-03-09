from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from BookListApp import views
app_name = 'BookListApp'
urlpatterns = [
    path(
        '',
        views.MainListView.as_view(),
        name = 'home',
    ),
    path(
        'delete/<int:pk>/',
        views.DeleteBookView.as_view(),
        name = 'delete'
    ),
    path(
        'create/',
        views.MainListView.as_view(),
        name = 'create'
    ),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
