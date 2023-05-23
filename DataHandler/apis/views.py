from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

#return render(request, HTML_FILE, {"PARAMETER":VALUE_HERE})
#return HttpResponse({status: 200, payload:DICTONARY_FILE})
#return HttpResponse("TEXT_HERE")

def home(request):
    return HttpResponse("You are at Home")
