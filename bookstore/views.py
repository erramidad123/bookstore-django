from django.shortcuts import render

from django.http import HttpResponse


from .models import * 



def home(request) : 
    return render(request,'bookstore/dashboard.html')


def books(request) :
    books = Book.objects.all() 

    return render(request,'bookstore/books.html',{'books':books})



def customers(request) :
    return render(request,'bookstore/customers.html')

def orders(request) :
    return render(request,'bookstore/orders.html')


