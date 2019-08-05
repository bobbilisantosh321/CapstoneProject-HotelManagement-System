from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.db import connection


# Create your views here.

def laundrylisting(request):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM laundry, booking, room, customer_customer WHERE booking_id = laundry_booking_id AND booking_room_id = room_id AND booking_customer_id = customer_id")
    laundrylist = dictfetchall(cursor)

    context = {
        "laundrylist": laundrylist
    }

    # Message according Laundry #
    context['heading'] = "Laundry Details";
    return render(request, 'laundry-view.html', context)


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
    cursor.execute("SELECT * FROM laundry WHERE laundry_id = " + id)
    dataList = dictfetchall(cursor)
    return dataList[0];

def update(request, laundryId):
    context = {
        "fn": "update",
        "bookinglist": getDropDown('booking', 'booking_id'),
        "laundryDetails": getData(laundryId),
        "heading": 'Laundry Update',
    }
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
                   UPDATE laundry
                   SET laundry_booking_id=%s, laundry_date=%s, laundry_amount=%s, laundry_description=%s WHERE laundry_id = %s
                """, (
            request.POST['laundry_booking_id'],
            request.POST['laundry_date'],
            request.POST['laundry_amount'],
            request.POST['laundry_description'],
            laundryId
        ))
        context["laundryDetails"] =  getData(laundryId)
        messages.add_message(request, messages.INFO, "Laundry updated succesfully !!!")
        return redirect('laundrylisting')
    else:
        return render(request, 'laundry.html', context)




def add(request):
    context = {
        "fn": "add",
        "bookinglist": getDropDown('booking', 'booking_id'),
        "heading": 'Laundry Details'
    };
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
		   INSERT INTO laundry
		   SET laundry_booking_id=%s, laundry_date=%s, laundry_amount=%s, laundry_description=%s		   
		""", (
            request.POST['laundry_booking_id'],
            request.POST['laundry_date'],
            request.POST['laundry_amount'],
            request.POST['laundry_description']))
        return redirect('laundrylisting')
    return render(request, 'laundry.html', context)


def delete(request, id):
    cursor = connection.cursor()
    sql = 'DELETE FROM laundry WHERE laundry_id=' + id
    cursor.execute(sql)
    return redirect('laundrylisting')
