import requests
from django.shortcuts import render, redirect
from .models import City   

def show_city(request):
    url ='https://api.openweathermap.org/data/2.5/weather?q={},&units=metric&APPID=a1fbdcfffceb8f51e1e7f282d6c462df'
    cities = City.objects.all()
    city = request.POST.get('city')
    if request.POST:
        if City.objects.filter(city = city): 
            return redirect('/')
        else:
            City.objects.create(city=city)
            return redirect('/')

    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.city,
            'temp': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    data = {'weather_data' : weather_data}
    return render(request,'index.html',data)

def delete_city(request,city):
        City.objects.get(city=city).delete()
        return redirect('/')
