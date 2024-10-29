
from django.urls import path,include
from .views import *
urlpatterns = [
    path('books/',BookListCreateView.as_view(),name='Book-list-create'),
    path('books/<int:pk>/',BookRetrieveUpdateDeleteView.as_view(),name='book-detail'),
   

]
