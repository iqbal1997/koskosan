from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    context={
        'title': 'Home',
    }
    return render(request,'Home.html',context)