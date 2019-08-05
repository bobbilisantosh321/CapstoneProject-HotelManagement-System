from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.db import connection


# Create your views here.

def billinglisting(request):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM billing, booking, room, customer_customer WHERE booking_id = billing_booking_id AND booking_room_id = room_id AND booking_customer_id = customer_id")
    billinglist = dictfetchall(cursor)

    context = {
        "billinglist": billinglist
    }

    # Message according Billing #
    context['heading'] = "Billing Details";
    return render(request, 'billing-view.html', context)


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def getDropDown(table, condtion):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM " + table + " WHERE " + condtion)
    dropdownList = dictfetchall(cursor)
    return dropdownList;


def getData(id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM billing WHERE billing_id = " + id)
    dataList = dictfetchall(cursor)
    return dataList[0];

def update(request, billingId):
    context = {
        "fn": "update",
        "bookinglist": getDropDown('booking', 'booking_id'),
        "billingDetails": getData(billingId),
        "heading": 'Billing Update',
    }
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
                   UPDATE billing
                   SET billing_booking_id=%s, billing_date=%s, billing_room_rent=%s, billing_food_bill=%s, billing_laundry_bill=%s, billing_description=%s WHERE billing_id = %s
                """, (
             request.POST['billing_booking_id'],
            request.POST['billing_date'],
            request.POST['billing_room_rent'],
            request.POST['billing_food_bill'],
            request.POST['billing_laundry_bill'],
            request.POST['billing_description'],
            billingId
        ))
        context["billingDetails"] =  getData(billingId)
        messages.add_message(request, messages.INFO, "Billing updated succesfully !!!")
        return redirect('billinglisting')
    else:
        return render(request, 'billing.html', context)




def add(request):
    context = {
        "fn": "add",
        "bookinglist": getDropDown('booking', 'booking_id'),
        "heading": 'Billing Details'
    };
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
		   INSERT INTO billing
		   SET billing_booking_id=%s, billing_date=%s, billing_room_rent=%s, billing_food_bill=%s, billing_laundry_bill=%s, billing_description=%s		   
		""", (
            request.POST['billing_booking_id'],
            request.POST['billing_date'],
            request.POST['billing_room_rent'],
            request.POST['billing_food_bill'],
            request.POST['billing_laundry_bill'],
            request.POST['billing_description']))
        return redirect('billinglisting')
    return render(request, 'billing.html', context)


def delete(request, id):
    cursor = connection.cursor()
    sql = 'DELETE FROM billing WHERE billing_id=' + id
    cursor.execute(sql)
    return redirect('billinglisting')
