
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.context_processors import csrf
=======
import json
import requests

# Create your views here.
def index(request):
    schedule = ["hello", "world"]

    url = "http://www.wsdot.wa.gov/Ferries/API/Schedule/rest/scheduletoday/6/false?apiaccesscode=d71bf03a-96aa-47cf-9fd1-25ec97e89d93"
    terminal_combinations = requests.get(url).json().get(u'TerminalCombos')
    kingston_departures= terminal_combinations[1]

    terminal_id = kingston_departures.get('DepartingTerminalID')

    times = kingston_departures.get(u'Times')

    departures = list()
    for time in times:
        departures.append(time.get('DepartingTime'))

    # need terminal ID and departure time
    context = { "schedule":departures, "terminal_id":terminal_id }
    return render(request, 'ferrytime/index.html', context)

def forecast(request):
    terminal_id = request.get('terminal_id')
    selected_time = request.get('time')

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
