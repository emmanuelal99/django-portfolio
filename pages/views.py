from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'pages/home.html', {})

def contact(request):
    if request.method == "POST":
        # Handle form submission here
        messages.success(request, 'Thank you for your message. We will get back to you soon!')
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')


        # Send email
        try:
            send_mail(
                f'Contact Form Submission from {name}',
                f'Message from {name} ({email}):\n\n{message}',
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],  # Send to yourself
                fail_silently=False,
            )
            messages.success(request, 'Thank you for your message. We will get back to you soon!')
        except Exception as e:
            messages.error(request, 'Sorry, there was an error sending your message. Please try again later.')
        return HttpResponseRedirect(reverse('home') + '#contact')
    else:
        return render(request, 'pages/contact.html', {})
            
            

            
        
        
