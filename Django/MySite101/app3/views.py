from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # we want to display html file
    # rendering html document
    # return HttpResponse("Hello from App3")
    return render(request, 'First.html')