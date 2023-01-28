from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import OrderForm,CreateNewUser
from .models import * 
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login , logout 
from .decorators import notLoggedUser, allowedUsers,forAdmins
from django.contrib.auth.models import Group

@login_required(login_url='login')
# @allowedUsers(allowedUsers=['admin'])
@forAdmins
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

@login_required(login_url='login')
def books(request) :
    books = Book.objects.all() 

    return render(request,'bookstore/books.html',{'books':books})


@login_required(login_url='login')
def customer(request,c_id) :
    customer = Customer.objects.get(id=c_id)
    orders = customer.order_set.all()

    searchFilter = OrderFilter(request.GET,queryset=orders) 
    orders = searchFilter.qs

    t_orders = orders.count() 
    return render(request,'bookstore/customers.html',{'customer':customer,'orders':orders,'t_orders':t_orders,'searchFilter':searchFilter})
@login_required(login_url='login')
def orders(request) :
    return render(request,'bookstore/orders.html')
@login_required(login_url='login')
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




@login_required(login_url='login')
@allowedUsers(allowedUsers=['admin'])
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


@login_required(login_url='login')
@allowedUsers(allowedUsers=['admin'])
def delete(request,order_id) : 
    order = Order.objects.get(id = order_id)
    if request.method == 'POST' : 
        order.delete() 
        return redirect('home')
    return render(request, 'bookstore/delete_form.html')


@notLoggedUser
def userLogin(request) :
    if request.user.is_authenticated : 
        return redirect('home')
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,' Welcome ' + user.username)
            return redirect('home')
        else : 
            messages.info(request,'Credentials not valid ')
    context = {}
    return render(request,'bookstore/login.html', context )

def userLogout(request) : 
    logout(request) 
    return redirect('login')







@notLoggedUser
def register(request) :
    form = UserCreationForm() 
    if request.method == 'POST' :
        form = CreateNewUser(request.POST) 
        if form.is_valid() : 
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name="customer")
            user.groups.add(group) 
            messages.success(request, username + ' account created successfully ')
            return redirect('login')
    context = {'form':form}
    return render(request,'bookstore/register.html', context )
      
@login_required(login_url='login')
@allowedUsers(allowedUsers=['customer'])
def userProfile(request) : 
    orders = request.user.customer.order_set.all() 
    context = {'orders': orders}
   
    return render(request,'bookstore/profile.html',context)