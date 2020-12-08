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
    person.full_name = full_name
    person.contact_address = contact_address
    person.save()# Call Save Method
    return HttpResponseRedirect("..")

# HW - EDIT Form and Update Record
def display_edit_form(request):
    #persons = Person.objects.all(); # Retrive all records from table
    #print(persons)
    tmp_id = request.GET.get('pid') # Getting value from Link (Edit Link)
    person = Person.objects.get(pid=tmp_id) # Gettring record from datanase
    print(person)
    return render(request, 'app8_1/edit.html', {'person': person})

def update_person(request):
    # Receive values from Form
    pid = request.POST.get('txt_id')
    full_name = request.POST.get('txt_name')
    contact_address = request.POST.get('txt_address')

    person = Person.objects.get(pid=pid)  # Gettring record from datanase
    person.full_name=full_name # Set New Value
    person.contact_address=contact_address # Set New Value
    person.save() # Update
    return HttpResponseRedirect("..")

def delete_person(request):
    tmp_id = request.GET.get('pid')  # Getting value from Link (Edit Link)
    person = Person.objects.get(pid=tmp_id) # Record Search and Get
    person.delete() # Record Delete
    return HttpResponseRedirect("..")