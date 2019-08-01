from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from apps.login_regist_app.models import User


# Create your views here.

def index(request):
    all_messages = Message.objects.all()
    all_comments = Comment.objects.all()
    context = {
        'all_messages':all_messages,
        'all_comments':all_comments,
    }

    return render(request,'wall_app/index.html',context)

def post_message(request):
    user = User.objects.get(id=request.session['user_id'])
    Message.objects.create(
        message=request.POST['message'],
        user= user        
    )
    message = Message.objects.last()
    message.save()
    return redirect('/wall')

def post_comment(request):
    user = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=request.POST['message_id'])
    Comment.objects.create(
        comment=request.POST['comment'],
        user= user,
        message = message,

    )

    return redirect('/wall')

def destroy_message(request, message_id):
    message = Message.objects.get(id=message_id)
    message.delete()
    return redirect('/wall')

def destroy_comment(request, comment_id):
    message = Comment.objects.get(id=comment_id)
    message.delete()
    return redirect('/wall')