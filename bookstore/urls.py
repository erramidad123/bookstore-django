from django.urls import path 

from . import views


urlpatterns = [
    path('', views.home,name='home'), 
    path('books/',views.books,name='books'),
    path('customer/<int:c_id>',views.customer,name='customer'), 
    path('orders/',views.orders,name='orders'),
    path('create/',views.create,name = 'create')

]


