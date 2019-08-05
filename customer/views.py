from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db import connection
from django.contrib import messages
from Customer import Customer
customerObj = Customer()

# Create your views here.
def index(request):
    return render(request,'login.html')

# Create your views here.
def customerlisting(request):
    context = {
        "customerlist": customerObj.listing()
    }
    context['heading'] = "All Customer Record";
    return render(request,'customer-record.html', context)

def getDropDown(table, condtion):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM " + table + " WHERE " + condtion)
    dropdownList = dictfetchall(cursor)
    return dropdownList;

def getData(id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customer_customer WHERE customer_id = " + id)
    dataList = dictfetchall(cursor)
    return dataList[0];

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def update(request, customerId):
    context = {
        "fn": "update",
        "customerdetails": getData(customerId),
        "heading": 'Customer Update',
    }
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
                   UPDATE customer_customer
		   SET customer_first_name=%s, customer_middle_name=%s,
		   customer_last_name=%s, customer_gender=%s, customer_address=%s, customer_village=%s, customer_mobile=%s,
		   customer_email=%s, customer_dob=%s, customer_nationalty=%s
		 WHERE customer_id=%s""", (
            request.POST['customer_first_name'],
            request.POST['customer_middle_name'],            
            request.POST['customer_last_name'],
            request.POST['customer_gender'],
            request.POST['customer_address'],
            request.POST['customer_village'],
            request.POST['customer_mobile'],
            request.POST['customer_email'],
            request.POST['customer_dob'],
            request.POST['customer_nationalty'],
            customerId
        ))
        context["customerdetails"] =  getData(customerId)
        messages.add_message(request, messages.INFO, "Customer updated succesfully !!!")
        return redirect('customerlisting')
    else:
        return render(request, 'customer-add.html', context)

def add(request):
    context = {
        "fn": "add",
        "heading": 'Add Customer'
    };
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
		   INSERT INTO customer_customer
		   SET customer_first_name=%s, customer_middle_name=%s,
		   customer_last_name=%s, customer_gender=%s, customer_address=%s, customer_village=%s, customer_mobile=%s,
		   customer_email=%s, customer_dob=%s, customer_nationalty=%s
		""", (
            request.POST['customer_first_name'],
            request.POST['customer_middle_name'],            
            request.POST['customer_last_name'],
            request.POST['customer_gender'],
            request.POST['customer_address'],
            request.POST['customer_village'],
            request.POST['customer_mobile'],
            request.POST['customer_email'],
            request.POST['customer_dob'],
            request.POST['customer_nationalty']))
        return redirect('customerlisting')
    return render(request, 'customer-add.html', context)



def delete(request, id):
    customerObj.delete(id)
    return redirect('customerlisting')
