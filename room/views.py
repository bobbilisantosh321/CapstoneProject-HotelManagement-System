from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.db import connection


# Create your views here.

def roomlisting(request):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM room")
    roomlist = dictfetchall(cursor)

    context = {
        "roomlist": roomlist
    }

    # Message according Room #
    context['heading'] = "Room Details";
    return render(request, 'room-view.html', context)


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
    cursor.execute("SELECT * FROM room WHERE room_id = " + id)
    dataList = dictfetchall(cursor)
    return dataList[0];

def update(request, roomId):
    context = {
        "fn": "update",
        "roomDetails": getData(roomId),
        "heading": 'Room Update',
    }
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
                   UPDATE room
                   SET room_number=%s, room_cost=%s, room_type=%s, room_description=%s WHERE room_id = %s
                """, (
            request.POST['room_number'],
            request.POST['room_cost'],
            request.POST['room_type'],
            request.POST['room_description'],
            roomId
        ))
        context["roomDetails"] =  getData(roomId)
        messages.add_message(request, messages.INFO, "Room updated succesfully !!!")
        return redirect('roomlisting')
    else:
        return render(request, 'room.html', context)




def add(request):
    context = {
        "fn": "add",
        "heading": 'Room Details'
    };
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
		   INSERT INTO room
		   SET room_number=%s, room_cost=%s, room_type=%s, room_description=%s		   
		""", (
            request.POST['room_number'],
            request.POST['room_cost'],
            request.POST['room_type'],
            request.POST['room_description']))
        return redirect('roomlisting')
    return render(request, 'room.html', context)


def delete(request, id):
    cursor = connection.cursor()
    sql = 'DELETE FROM room WHERE room_id=' + id
    cursor.execute(sql)
    return redirect('roomlisting')
