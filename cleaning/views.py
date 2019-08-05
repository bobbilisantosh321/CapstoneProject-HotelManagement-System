from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.db import connection


# Create your views here.

def cleaninglisting(request):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM cleaning, room WHERE room_id = cleaning_room_id")
    cleaninglist = dictfetchall(cursor)

    context = {
        "cleaninglist": cleaninglist
    }

    # Message according Cleaning #
    context['heading'] = "Cleaning Details";
    return render(request, 'cleaning-view.html', context)


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
    cursor.execute("SELECT * FROM cleaning WHERE cleaning_id = " + id)
    dataList = dictfetchall(cursor)
    return dataList[0];

def update(request, cleaningId):
    context = {
        "fn": "update",
        "roomlist": getDropDown('room', 'room_id'),
        "cleaningDetails": getData(cleaningId),
        "heading": 'Cleaning Update',
    }
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
                   UPDATE cleaning
                   SET cleaning_room_id=%s, cleaning_date=%s, cleaning_description=%s WHERE cleaning_id = %s
                """, (
            request.POST['cleaning_room_id'],
            request.POST['cleaning_date'],
            request.POST['cleaning_description'],
            cleaningId
        ))
        context["cleaningDetails"] =  getData(cleaningId)
        messages.add_message(request, messages.INFO, "Cleaning updated succesfully !!!")
        return redirect('cleaninglisting')
    else:
        return render(request, 'cleaning.html', context)




def add(request):
    context = {
        "fn": "add",
        "roomlist": getDropDown('room', 'room_id'),
        "heading": 'Cleaning Details'
    };
    if (request.method == "POST"):
        cursor = connection.cursor()
        cursor.execute("""
		   INSERT INTO cleaning
		   SET cleaning_room_id=%s, cleaning_date=%s, cleaning_description=%s		   
		""", (
            request.POST['cleaning_room_id'],
            request.POST['cleaning_date'],
            request.POST['cleaning_description']))
        return redirect('cleaninglisting')
    return render(request, 'cleaning.html', context)


def delete(request, id):
    cursor = connection.cursor()
    sql = 'DELETE FROM cleaning WHERE cleaning_id=' + id
    cursor.execute(sql)
    return redirect('cleaninglisting')
