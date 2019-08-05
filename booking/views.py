from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.db import connection


# Create your views here.

def bookinglisting(request):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM booking, customer_customer, room WHERE room_id = booking_room_id AND booking_customer_id = customer_id")
    bookinglist = dictfetchall(cursor)

    context = {
        "bookinglist": bookinglist
    }

    # Message according Booking #
    context['heading'] = "Booking Details";
    return render(request, 'booking-view.html', context)

def cancellisting(request):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM booking, customer_customer, room, status WHERE status_id = booking_status AND room_id = booking_room_id AND booking_customer_id = customer_id AND booking_status = 3")
    bookinglist = dictfetchall(cursor)

    context = {
        "bookinglist": bookinglist
    }

    # Message according Booking #
    context['heading'] = "Booking Details";
    return render(request, 'cancel-view.html', context)


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
    cursor.execute("SELECT * FROM booking WHERE booking_id = " + id)
    dataList = dictfetchall(cursor)
    return dataList[0];

def update(request, bookingId):
    context = {
        "fn": "update",
        "customerlist": getDropDown('customer_customer', 'customer_id'),
        "roomlist": getDropDown('room', 'room_id'),
        "bookingDetails": getData(bookingId),
        "statuslist": getDropDown('status', 'status_id'),
        "heading": 'Booking Update',
    }
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
                   UPDATE booking
                   SET booking_room_id=%s, booking_customer_id=%s, booking_from_date=%s, booking_to_date=%s, booking_status=%s, booking_amount=%s, booking_description=%s WHERE booking_id = %s
                """, (
            request.POST['booking_room_id'],
            request.POST['booking_customer_id'],
            request.POST['booking_from_date'],
            request.POST['booking_to_date'],
            request.POST['booking_status'],
            request.POST['booking_amount'],
            request.POST['booking_description'],
            bookingId
        ))
        context["bookingDetails"] =  getData(bookingId)
        messages.add_message(request, messages.INFO, "Booking updated succesfully !!!")
        return redirect('bookinglisting')
    else:
        return render(request, 'booking.html', context)




def add(request):
    context = {
        "fn": "add",
        "customerlist": getDropDown('customer_customer', 'customer_id'),
        "statuslist": getDropDown('status', 'status_id'),
        "roomlist": getDropDown('room', 'room_id'),
        "heading": 'Booking Details'
    };
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
		   INSERT INTO booking
		   SET booking_room_id=%s, booking_customer_id=%s, booking_from_date=%s, booking_to_date=%s, booking_status=%s, booking_amount=%s, booking_description=%s		   
		""", (
            request.POST['booking_room_id'],
            request.POST['booking_customer_id'],
            request.POST['booking_from_date'],
            request.POST['booking_to_date'],
            request.POST['booking_status'],
            request.POST['booking_amount'],
            request.POST['booking_description']))
        return redirect('bookinglisting')
    return render(request, 'booking.html', context)


def delete(request, id):
    cursor = connection.cursor()
    sql = 'DELETE FROM booking WHERE booking_id=' + id
    cursor.execute(sql)
    return redirect('bookinglisting')
