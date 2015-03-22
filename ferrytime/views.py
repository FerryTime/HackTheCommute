from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.context_processors import csrf
import json
import requests
from datetime import datetime
from django.http import Http404
from django.http import HttpResponse

rest_host = "http://www.wsdot.wa.gov/"
rest_base = ''.join([rest_host,"Ferries/API/Schedule/rest/"])
payload = {'apiaccesscode': 'd71bf03a-96aa-47cf-9fd1-25ec97e89d93'}

def index(request):
    schedule_url = ''.join([rest_base,"scheduletoday/6/false"])
    result_json = requests.get(schedule_url, params=payload).json()
    terminal_combinations = result_json.get(u'TerminalCombos')
    kingston_departures = terminal_combinations[1]

    terminal_id = kingston_departures.get(u'DepartingTerminalID')

    times = kingston_departures.get(u'Times')

    departure_times = list()

    for time in times:
        json_date = time.get('DepartingTime')
        milliseconds_since_epoch_tz = int(json_date[6:-7])
        hours_gmt_offset = int(json_date[-7:-4])
        seconds_since_epoch_tz = milliseconds_since_epoch_tz / 1000
        seconds_gmt_offset = 60 * 60 * hours_gmt_offset
        seconds_since_epoch = seconds_since_epoch_tz + seconds_gmt_offset
        d = datetime.fromtimestamp(seconds_since_epoch)
        departure_times.append(((str(d)),str(json_date)))

    # need terminal ID and departure time
    schedule = departure_times
    context = { "schedule":schedule, "terminal_id":terminal_id }
    return render(request, 'ferrytime/index.html', context)

def forecast(request):
    terminal_id = request.GET['terminal_id']
    selected_time = request.GET['time']

    forecast_url = ''.join([rest_base,"terminalsailingspace/", terminal_id])
    result = requests.get(forecast_url, params=payload)
    if result.status_code != 200 :
        return HttpResponse('Canada, eh?')
        # raise Http404("Canada, eh?")
    result_json = result.json()

    # DriveUpSpaceCount
    # filter with selected_time on DepartingSpaces:Departure
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
