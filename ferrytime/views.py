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
rest_base = ''.join([rest_host,"Ferries/API/"])
payload = {'apiaccesscode': 'd71bf03a-96aa-47cf-9fd1-25ec97e89d93'}

def index(request):
    schedule_url = ''.join([rest_base,"Schedule/rest/scheduletoday/6/false"])
    result_json = requests.get(schedule_url, params=payload).json()
    terminal_combinations = result_json.get(u'TerminalCombos')
    kingston_departures = terminal_combinations[1]
    terminal_id = None
    times = None

    for x in terminal_combinations:
        if x['DepartingTerminalName'] == 'Kingston':
            terminal_id = x['DepartingTerminalID']
            times = x['Times']
            break

    departure_times = list()
    for time in times:
        json_date = time.get('DepartingTime')
        d = datetime_from_asp_json(json_date)
        departure_times.append(((str(d)),str(json_date)))

    # need terminal ID and departure time
    schedule = departure_times
    context = { "schedule":schedule, "terminal_id":terminal_id }
    return render(request, 'ferrytime/index.html', context)

def forecast(request):
    terminal_id = request.GET['terminal_id']
    selected_time = request.GET['time']
    human_time = datetime_from_asp_json(selected_time)

    forecast_url = ''.join([rest_base,"Terminals/rest/terminalsailingspace/", str(terminal_id)])
    result = requests.get(forecast_url, params=payload)
    if result.status_code != 200 :
        return HttpResponse('<html><head><title>Sorry!</title></head><body>No current sailings.</body></html>')
    result_json = result.json()

    # filter with selected_time on DepartingSpaces:Departure
    departing_spaces = result_json.get(u'DepartingSpaces')

    drive_up_space_count = None
    vessel_name = str()
    vessel_id = str()
    max_space_count = int()

    for x in departing_spaces:
        if str(x[u'Departure']) == selected_time:
            drive_up_space_count = str(x['SpaceForArrivalTerminals'][0]['DriveUpSpaceCount'])
            vessel_name = str(x['SpaceForArrivalTerminals'][0]['VesselName'])
            vessel_id = str(x['SpaceForArrivalTerminals'][0]['VesselID'])
            max_space_count = int(x['SpaceForArrivalTerminals'][0]['MaxSpaceCount'])
            break

    # calculate percent and determine color based on it
    # drive_up_space_count / max_space_count
    percentage = drive_up_space_count / max_space_count
    if percentage > 0.60:
        bg_color = "#FF0000"
    elif 0.60 > percentage > 0.10:
        bg_color = "#FFFF66"
    elif 0.10 > percentage:
        bg_color = "#339966"

    context = {"space" : drive_up_space_count, "time": human_time, "vessel_name": vessel_name, "vessel_id": vessel_id, "bg_color": bg_color}

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
def login(request):
    pass

def datetime_from_asp_json(json_date):
    milliseconds_since_epoch_tz = int(json_date[6:-7])
    hours_gmt_offset = int(json_date[-7:-4])
    seconds_since_epoch_tz = milliseconds_since_epoch_tz / 1000
    seconds_gmt_offset = 60 * 60 * hours_gmt_offset
    seconds_since_epoch = seconds_since_epoch_tz + seconds_gmt_offset
    return(datetime.fromtimestamp(seconds_since_epoch))
