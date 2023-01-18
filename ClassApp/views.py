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
    return render(request, "home.html", context=data)

def results(request):
    results_data = dict()
    return render(request, "results.html", context = results_data)

"""def maintenance(request):
    maintenance_data = dict()
    try:
        choice = request.GET['selection']
        if choice == "currencies":
            support_functions.add_currencies(support_functions.get_currency_list())
            c_list = Currency.objects.all()
            print("Got c_list", len(c_list))
            data['currencies'] = c_list
            return HttpResponseRedirect(reverse('currencies'))
    except:
        pass
    return render(request, "maintenance.html", context=maintenance_data)"""


