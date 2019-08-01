from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
    user = User.objects.all()
    context = {
        'user':user
    }

    return render(request,'login_regist_app/index.html', context)



def registration(request):

    errors = User.objects.registration_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value,extra_tags="regist_error")
        return redirect('/')
    else:
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email =request.POST['email'],
            password=request.POST['password'],
            confirm_pass=request.POST['confirm_pass'],
        )
        print(f'////////CREATE////////')
        last_user_created = User.objects.last()
        request.session['user_id'] = last_user_created.id
        request.session['user_name']= last_user_created.first_name
        messages.success(request, 'Successfully registered!')
        
        return redirect('/success')

def login(request):

    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags="login_error")
        return redirect('/')
    else:
        
        user_to_login = User.objects.get(email=request.POST['email_login'])
        request.session['user_id'] = user_to_login.id
        request.session['user_name']= user_to_login.first_name
        messages.success(request, 'Successfully logged in!')
        
        return redirect('/wall')

def success(request):
    if 'user_id'not in request.session:
        return redirect('/')
    else:

        return render(request,'login_regist_app/success.html')

def logout(request):
    request.session.clear()
    return redirect('/')