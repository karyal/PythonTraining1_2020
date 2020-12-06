from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# Create your views here.
def index(request):
    persons = Person.objects.all()
    print(len(persons))
    context = {'persons': persons}
    return render(request, 'app8_1/index.html', context)