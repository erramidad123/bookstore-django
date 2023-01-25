from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def home(request) : 
    return render(request,'bookstore/dashboard.html')


def books(request) :
    return render(request,'bookstore/books.html')



def customers(request) :
    return render(request,'bookstore/customers.html')


