from django.shortcuts import render
import urllib.request
import json
# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST['city']
        resource = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=4ea650dcbb111f2b09b50e90340b3fbb')
        jsonData = json.load(resource)
        data = {
            "countryCode" : str(jsonData['sys']['country']),
            "coordinates" : str(jsonData['coord']['lon'])+","+str(jsonData['coord']['lat']),
            "temp" : str(jsonData['main']['temp']),
            "pressure" : str(jsonData['main']['pressure']),
            "humidity" : str(jsonData['main']['humidity']),
            
        }
        
        
    else:
        data = {}
        city = ''
    return render(request,'index.html',{'city':city,'data':data})