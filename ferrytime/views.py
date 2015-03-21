from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'ferrytime/index.html', context)

def forecast(request):
    context = {}
    return render(request, 'ferrytime/forecast.html', context)
