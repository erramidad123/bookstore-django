from django.urls import path 

from . import views


urlpatterns = [
    path('', views.home,name='home'), 
    path('books/',views.books,name='books'),
    path('customer/<int:c_id>',views.customer,name='customer'), 
    path('orders/',views.orders,name='orders'),
    path('create/',views.create,name = 'create'),
    path('update/<int:order_id>',views.update,name = 'update'),
    path('delete/<int:order_id>',views.delete,name = 'delete'),
    path('login/',views.userLogin,name='login'),
    path('register/',views.register,name = 'register'),
]


