from django.shortcuts import render
from django.http import HttpResponse
from pyowm import OWM
import urllib.request
def input(request):
    return render(request,'input.html')
def data(request):
    a=request.POST['t1']
    b=request.POST['t2']
    c=request.POST['t3']
    API_key = 'G097IueS-9xN712E'
    owm = OWM(API_key)
    API_key=owm.set_API_key('6Lp$0UY220_HaSB45')
    owm = OWM(API_key, version='2.5', config_module='mypackage.mysubpackage.myconfigmodule')
    a=urllib.request.urlopen('http://api.openweathemap.org/data/2.5/weather?appid=',API_key,a)
    b=a.read()
    c=b.decode('utf-8')
    e=d.split()
    location = owm.weather_at_place(a)
    temperature=owm.get_temperature(b)                  # ... or in Celsius
    date=owm.get_reception_time(c)
    return render(request,'data.html',{'l':location,'t':temperature,'d':date})
