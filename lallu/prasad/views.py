from django.shortcuts import render
from django.http import HttpResponse


def test(request):
    return render(request,'hello.html')

def index(request):
    return render(request,'index.html') 
