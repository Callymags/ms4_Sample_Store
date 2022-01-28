from django.shortcuts import render
from django.contrib import messages

def index(request):
    """ Return the index page """

    return render(request, 'home/index.html')
