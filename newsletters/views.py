from django.contrib import messages
from django.shortcuts import render, redirect, reverse

from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm
# Create your views here.

# Sign Up
def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 
            'Your email already exists in our database', 
            'alert alert-warning alert-dismissible')
        else:
            instance.save()
            messages.success(request,
                            'Your email has been submited to the database',
                            'alert alert-success alert-dismissible')


    context = {
        'form': form,
    }
    template = 'newsletters/sign_up.html'
    return render(request, template, context)


# Unsubscribe
def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request,
                            'Your email has been removed!',
                            'alert alert-success alert-dismissible')
        else:
            messages.warning(request,
                            'Your email is not in the database!',
                            'alert alert-warning alert-dismissible')

    context = {
        'form': form,
    }
    template = 'newsletters/unsubscribe.html'
    return render(request, template, context)
