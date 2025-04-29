from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def homeview(request):
    return render(request,'home.html')

def aboutview(request):
    return render(request,'about.html')

def contactview(request):
    if request.method == 'POST':
            username=request.POST['username']
            email=request.POST['email']
            messages_text=request.POST['messages']
            contact =Contact(username=username,email=email,messages=messages_text)
            contact.save()
            messages.success(request," Message Sent Successfully !!")
            send_mail(
            subject='Thank You for Contacting Us!',
            message=f'Hi {username},\n\nThanks for reaching out! We will get back to you soon.\n\n— Admin',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
            )
            return redirect('/contact/')
    return render(request,'contact.html')

