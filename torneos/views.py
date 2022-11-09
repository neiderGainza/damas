from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def torneos(request):

    return render( request , "torneos/torneos.html", {})
