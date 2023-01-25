from django.db import models

class Customer(models.Model) :
    name = models.CharField(max_length=100, null= True)
    email = models.CharField(max_length=200, null= True)
    phone = models.CharField(max_length=100, null= True)
    age = models.CharField(max_length=100, null= True)
    date = models.DateField(auto_now_add=True, null= True)
    
    def __str__(self) :
        return self.name 

class Tag(models.Model) :
    tag = models.CharField(max_length=100)
    def __str__(self) :
        return self.tag

class Book(models.Model) :
    CATEGORIES = (
        ('science','science'),
        ('fiction','fiction'),
        ('fantasy','fantasy'),
        ('comic','comic'),
    )
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null= True)
    price = models.FloatField()
    tags = models.ManyToManyField(Tag)
    category = models.CharField(max_length=100, null= True,choices=CATEGORIES)
    description = models.CharField(max_length=100, null= True)
    date = models.DateField(auto_now_add=True)
    def __str__(self) : 
        return self.name 



class Order(models.Model) : 
    STATUS = (
        ('Pending','Pending'),
        ('Delivered','Delivered'),
        ('out of order','out of order'),
        ('in progress','in progress'),

    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    book = models.ForeignKey(Book , on_delete=models.CASCADE,null=True)
    
    
    
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)
