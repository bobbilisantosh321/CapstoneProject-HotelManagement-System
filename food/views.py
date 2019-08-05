from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.db import connection


# Create your views here.

def foodlisting(request):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM food, booking, room, customer_customer WHERE booking_id = food_booking_id AND booking_room_id = room_id AND booking_customer_id = customer_id")
    foodlist = dictfetchall(cursor)

    context = {
        "foodlist": foodlist
    }

    # Message according Food #
    context['heading'] = "Food Details";
    return render(request, 'food-view.html', context)


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
    cursor.execute("SELECT * FROM food WHERE food_id = " + id)
    dataList = dictfetchall(cursor)
    return dataList[0];

def update(request, foodId):
    context = {
        "fn": "update",
        "bookinglist": getDropDown('booking', 'booking_id'),
        "foodDetails": getData(foodId),
        "heading": 'Food Update',
    }
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
                   UPDATE food
                   SET food_booking_id=%s, food_date=%s, food_amount=%s, food_description=%s WHERE food_id = %s
                """, (
            request.POST['food_booking_id'],
            request.POST['food_date'],
            request.POST['food_amount'],
            request.POST['food_description'],
            foodId
        ))
        context["foodDetails"] =  getData(foodId)
        messages.add_message(request, messages.INFO, "Food updated succesfully !!!")
        return redirect('foodlisting')
    else:
        return render(request, 'food.html', context)




def add(request):
    context = {
        "fn": "add",
        "bookinglist": getDropDown('booking', 'booking_id'),
        "heading": 'Food Details'
    };
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
		   INSERT INTO food
		   SET food_booking_id=%s, food_date=%s, food_amount=%s, food_description=%s		   
		""", (
            request.POST['food_booking_id'],
            request.POST['food_date'],
            request.POST['food_amount'],
            request.POST['food_description']))
        return redirect('foodlisting')
    return render(request, 'food.html', context)


def delete(request, id):
    cursor = connection.cursor()
    sql = 'DELETE FROM food WHERE food_id=' + id
    cursor.execute(sql)
    return redirect('foodlisting')
