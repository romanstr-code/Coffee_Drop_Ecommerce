from django.shortcuts import render


def index(request):
    """ A view to return the company about page """

    return render(request, 'about/about.html')
