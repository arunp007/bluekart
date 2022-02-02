from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blue(request):

    return render(request,'bluekart.html')