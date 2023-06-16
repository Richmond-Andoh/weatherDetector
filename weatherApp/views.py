from django.shortcuts import render
import json, urllib

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q="+city+'&appid=40ebc54474805e40df5eb9e1e00569f8').read()
        json_data = json.loads(res)
        data = {
            'city': city,
            'country_code': str(json_data['sys']['country']),
            'coord': str(json_data['coord']['lon']) + ' ' + ' ' + str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp']) + 'k',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
        }
    else:
        data = {}
    return render(request, 'index.html', data)