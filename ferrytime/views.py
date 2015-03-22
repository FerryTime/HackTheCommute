from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.context_processors import csrf

# Create your views here.
def index(request):
    context = {}
    return render(request, 'ferrytime/index.html', context)

def forecast(request):
    context = {}
    return render(request, 'ferrytime/forecast.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })
