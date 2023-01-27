from django.shortcuts import render,redirect


from django.http import HttpResponse
from .my_order_form import OrderForm
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



def customer(request,c_id) :
    customer = Customer.objects.get(id=c_id)
    orders = customer.order_set.all()
    t_orders = orders.count() 
    return render(request,'bookstore/customers.html',{'customer':customer,'orders':orders,'t_orders':t_orders})

def orders(request) :
    return render(request,'bookstore/orders.html')

def create(request) :

    form = OrderForm()

    if request.method == 'POST' :
        print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid() : 
            form.save()
            return redirect('home')
    
    
    
    
    context = { 
        'form':form
    }
    return render(request,'bookstore/my_order_form.html',context) 





def update(request,order_id) :
    order = Order.objects.get(id=order_id)
    form = OrderForm(instance=order)

    if request.method == 'POST' :
        form = OrderForm(request.POST,instance=order)
        if form.is_valid() :
            form.save() 

            return redirect('home')

    context = { 
        'form':form
    }
    return render(request,'bookstore/order_update.html',context) 



def delete(request,order_id) : 
    order = Order.objects.get(id = order_id)
    if request.method == 'POST' : 
        order.delete() 
        return redirect('home')
    return render(request, 'bookstore/delete_form.html')