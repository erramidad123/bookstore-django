from django.shortcuts import render

from django.http import HttpResponse


from .models import * 



def home(request) : 
    orders = Order.objects.all() 
    customers = Customer.objects.all() 
    total_orders = orders.count()
    pending_orders = orders.filter(status='Pending').count()
    delivered_orders = orders.filter(status='Delivered').count()
    inprogress_orders = orders.filter(status='in progress').count()
    out_orders = orders.filter(status='out of order').count()

    data = {
        'total_orders' : total_orders, 
        'pending_orders' : pending_orders, 
        'delivered_orders' : delivered_orders, 
        'out_orders' : out_orders,

    }
    

    return render(request,'bookstore/dashboard.html',{'orders':orders,'customers':customers,'data':data})


def books(request) :
    books = Book.objects.all() 

    return render(request,'bookstore/books.html',{'books':books})



def customers(request) :
    return render(request,'bookstore/customers.html')

def orders(request) :
    return render(request,'bookstore/orders.html')


