from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import user
from django.contrib import messages
from django.db import connection


# Create your views here.
def index(request):
    if(request.session.get('authenticated', False) == True):
        return redirect('/users/dashboard')

    context = {
        "message": "Please Log in",
        "error": False
    }
    if(request.method == "POST"):
        try:
            getUser = user.objects.get(user_username=request.POST['username'])
            context['msg'] = getUser
        except:
            context['message'] = "Wrong username"
            context['error'] = True
            return render(request,'login.html', context)
        if(getUser.user_password == request.POST['password']):
            request.session['authenticated'] = True
            request.session['user_id'] = getUser.user_id
            request.session['user_name'] = getUser.user_name
            return redirect('/users/dashboard')
        else:
            context['message'] = "Wrong Password"
            context['error'] = True
            return render(request,'login.html', context)
    else:
        return render(request,'login.html', context)		
		
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]		
		
def listing(request):
        return render(request,'dashboard.html')

def forgot(request):
    return render(request,'forgotpass.html')

def logout(request):
    request.session['authenticated']= False
    request.session['user_id'] = False
    request.session['user_name']= False
    return redirect('/')

def changepassword(request):
    if (request.method == "POST"):
        try:
            addUser = user(
                user_id = request.session.get('user_id', None),
                user_password = request.POST['user_new_password']
            )
            addUser.save(update_fields=["user_password"])
        except Exception, e:
            return HttpResponse('Something went wrong. Error Message : '+ str(e))
        messages.add_message(request, messages.INFO, "Your Password has been changed successfully !!!")
        return render(request,'change-password.html')

    else:
        return render(request,'change-password.html')
    return render(request,'change-password.html')
