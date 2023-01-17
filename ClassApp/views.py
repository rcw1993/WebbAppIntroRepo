from django.shortcuts import render

# Create your views here.
def home(request):
    data = dict()
    import datetime
    time = datetime.datetime.now()
    print(time)
    data["time_of_day"] = time
    #diff = timedelta(hour=-5)
    #data["time_of_day"].hour = (data["time_of_day"].hour + 7) % 12
    return render(request, "home.html", context=data)
