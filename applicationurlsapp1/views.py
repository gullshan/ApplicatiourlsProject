from django.shortcuts import render
from django.http import HttpResponse
def input(request):
    return render(request,'base1.html')
def mul(request):
    try:
        a=request.GET['t1']
        x=int(a)
        b=request.GET['t2']
        y=int(b)
        z=x*y
        return HttpResponse("<html><body bgcolor=red><h1>mul is:"+str(z)+"</h1></body></html>")
    except(ValueError):
        return HttpResponse("invalid input")