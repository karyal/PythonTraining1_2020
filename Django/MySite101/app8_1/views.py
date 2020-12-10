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

def crud_model(request):
    # print("Hello from crud_model function of views")

# Insert Record
    # Data Source  -> Web Form
    #              -> URL
    #              -> Data File
    #              -> Database

    person1 = Person()
    person1.pid=2 # if pid=2 already inserted ; record will update (edit)
    person1.full_name="Bikash Khanal"
    person1.contact_address = "Ktm"
    person1.save()

    person2 = Person(pid=3, full_name="Devi Sunuwar", contact_address="Ktm")
    person2.save()

    person2 = Person(pid=4, full_name="Raju Thapa", contact_address="Bkh")
    person2.save()

    person2 = Person(pid=5, full_name="Reeta Rai", contact_address="Bhk")
    person2.save()

    person2 = Person(pid=6, full_name="Rupesh Shrestha", contact_address="Ktm")
    person2.save()

    person2 = Person(pid=7, full_name="Prakash Rawat", contact_address="Dang")
    person2.save()

    person2 = Person(pid=8, full_name="Ashok Rawat", contact_address="Puthan")
    person2.save()

    person2 = Person(pid=9, full_name="Tanks Adhikari", contact_address="Dolpa")
    person2.save()

    person2 = Person(pid=10, full_name="Ashirya Tuladhar", contact_address="Ktm")
    person2.save()

# Select Record
    # Select All Records
    persons = Person.objects.all()
    #print(persons)
    """
    for person in persons:
        print(person)
    """
    # Get Record
    #person1 = Person.objects.get(pid=10)
    #print(person1)

    # Filter Record/Search
    print("Filter")
    result = Person.objects.filter(pid=1)
    result = Person.objects.filter(pid__exact=10)
    result = Person.objects.filter(pid__gt=5)
    result = Person.objects.filter(pid__gte=5)
    result = Person.objects.filter(pid__lt=5)
    result = Person.objects.filter(pid__lte=5)

    result = Person.objects.filter(full_name="Krishna Aryal")
    result = Person.objects.filter(full_name__exact="Krishna Aryal")
    result = Person.objects.filter(full_name__startswith="R")
    result = Person.objects.filter(full_name__endswith="l")
    result = Person.objects.filter(full_name__contains="sh")

    result = Person.objects.exclude(pid=5)
    result = Person.objects.exclude(contact_address__contains="K")
    result = Person.objects.exclude(pid__in=[2, 3, 4, 5, 6])
    result = Person.objects.filter(pid__in=[2, 3, 4, 5, 6])

    # Order
    result = Person.objects.all().order_by('pid')# ASC
    result = Person.objects.all().order_by('-pid')  # DESC
    result = Person.objects.all().order_by('-pid').order_by('-full_name') # DESC

    # Result to Dictionary
    result = Person.objects.values()

    # Result to List
    result = Person.objects.all()

# Update
    # Individual Record Update
    person  = Person()
    person.pid=1
    person.full_name="Keshor Thapa"
    person.save()

    person = Person.objects.get(pid=1)
    print(person)

    person = Person(pid=2, full_name="Raju Mahat", contact_address="Birjung")
    person.save()
    person = Person.objects.get(pid=2)
    print(person)

    # Bulk Update
    Person.objects.select_for_update().filter(contact_address="Ktm").update(contact_address="Kathmandu, Nepal")
    print(result)

# Delete Record
    # Individual Delete
    # person  = Person.objects.get(pid=11)
    # person.delete()

    # Bulk Delete
    # Person.objects.select_for_update().filter(contact_address="Ktm").delete()

    return HttpResponse("Hello from crud_model")