from django.urls import path 

from . import views


urlpatterns = [
    path('', views.home,name='home'), 
    path('books/',views.books,name='books'),
    path('customers/',views.customers,name='customers'), 
]


