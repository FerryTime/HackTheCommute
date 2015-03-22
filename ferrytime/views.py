from django.shortcuts import render
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
    context = { "schedule":departures }
    return render(request, 'ferrytime/index.html', context)

def forecast(request):
    context = {}
    return render(request, 'ferrytime/forecast.html', context)
