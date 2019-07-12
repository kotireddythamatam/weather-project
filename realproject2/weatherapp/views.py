from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
def input(request):
    return render(request,'input.html')
def data(request):
    a=request.POST['t1']
    b=request.POST['t2']
    c=request.POST['t3']
    a=urllib.request.urlopen('http://api.openweathemap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='+a)
    b=a.read()
    c=b.decode('utf-8')
    e=d.split()
    f=[]
    for i in e:
        h=i.split()
        f.append(h)
    return render(request,'data.html',{'f1:'f})
    
