from django.shortcuts import render, redirect
from .forms import SubscribersForm

def index(request):
    """ Return the index page """
    if request.method =='POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SubscribersForm()
    context = {
        'form': form,
    }
    return render(request, 'home/index.html', context)