
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.context_processors import csrf
import json
import requests
from datetime import datetime

# Create your views here.
def index(request):
    schedule = ["hello", "world"]

    url = "http://www.wsdot.wa.gov/Ferries/API/Schedule/rest/scheduletoday/6/false?apiaccesscode=d71bf03a-96aa-47cf-9fd1-25ec97e89d93"
    terminal_combinations = requests.get(url).json().get(u'TerminalCombos')
    kingston_departures= terminal_combinations[1]

    terminal_id = kingston_departures.get(u'DepartingTerminalID')

    times = kingston_departures.get(u'Times')

    departures = list()
    for time in times:
        timeIn = time.get('DepartingTime')
        timeSlice = int(timeIn[6:-7])
        offset = int(timeIn[-5:-6])
        d = datetime.fromtimestamp(timeSlice/1000.00)
        departures.append(str(d))

    # need terminal ID and departure time
    context = { "schedule":departures, "terminal_id":terminal_id }
    return render(request, 'ferrytime/index.html', context)

def forecast(request):
    terminal_id = request.GET['terminal_id']
    selected_time = request.GET['time']

    url = "http://www.wsdot.wa.gov/Ferries/API/Terminals/rest/terminalsailingspace?apiaccesscode=ffd8b8c2-c4e6-4784-a9df-2b8f7ee6dfc5"
    terminal_combinations = requests.get(url).json().get(u'TerminalCombos')
    kingston_departures= terminal_combinations[1]

    terminal_id = kingston_departures.get(u'DepartingTerminalID')

    data = kingston_departures.get(u'SpaceForArrivalTerminals')

    driveUp = list()
    for space in spaces:
        driveUp.append(space.get(u'DriveUpSpaceCount'))

    context = {"space":driveUp}

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
