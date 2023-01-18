from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    data = dict()
    import datetime
    time = datetime.datetime.now()
    print(time)
    data["time_of_day"] = time

    ingredients_data = dict()
    choice = 'NONE'
    try:
        choice = request.GET['selection']
        choice = [choice]
        return HttpResponseRedirect(reverse(choice))
    except:
        pass
    return render(request, "home.html", context=data)

def results(request):
    results_data = dict()
    return render(request, "results.html", context = results_data)

def maintenance(request):
    maintenance_data = dict()
    choice = 'NONE'
    try:
        choice = request.GET['selection']
        choice = [choice]
    except:
        pass
    print(choice)
    return render(request, "maintenance.html", context=maintenance_data)


