from django.shortcuts import render
import json
import requests

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
        departures.append(time.get(u'DepartingTime'))

    # need terminal ID and departure time
    context = { "schedule":departures }
    return render(request, 'ferrytime/index.html', context)

def forecast(request):
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
