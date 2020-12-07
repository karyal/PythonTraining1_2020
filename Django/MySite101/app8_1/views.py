from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Person

# Create your views here.
def index(request):
    persons = Person.objects.all()
    print(len(persons))
    context = {'persons': persons}
    return render(request, 'app8_1/index.html', context)

def display_new_form(request):
    return render(request, 'app8_1/new.html')

def save_new_person(request):

    # Receive values from Form
    pid = request.POST.get('txt_id')
    full_name  = request.POST.get('txt_name')
    contact_address = request.POST.get('txt_address')

    # Process for Save
    person = Person() # Object of Model Class
    person.pid = pid # Set Value
    person.full_name=full_name
    person.contact_address = contact_address
    person.save()# Call Save Method
    return HttpResponseRedirect("..")