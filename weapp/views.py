from django.shortcuts import render
import json
import requests

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=3d271f6adf443ca8bc9f6d04a257b3cf'
        list_of_data = requests.get(url.format(city)).json()
        data={
        'co_ordinates' : str(list_of_data['coord']['lon']) + ',' + str(list_of_data['coord']['lat']),
        'condition': str(list_of_data['weather'][0]['main']),
        'description': str(list_of_data['weather'][0]['description']),
        'temperature': str(list_of_data['main']['temp']) + '°C',
        'wind': str(list_of_data['wind']['speed']),
        'humidity': str(list_of_data['main']['humidity']),
        }
       
    else:
        data = {}
    return render(request,'weather/weather.html',data)

