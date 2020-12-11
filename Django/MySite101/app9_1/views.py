from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import PersonForm
from .models import Person

def index(request):
    return HttpResponse("Hello from app9_1")


def display_form_1(request):
    form1 = PersonForm()
    return render(request, 'app9_1/display_form1.html', {'form1': form1})


def get_form_1(request):
    full_name = request.POST.get('full_name')
    contact_address = request.POST.get('contact_address')
    email = request.POST.get('email')
    mobile = request.POST.get('mobile')

    person = Person()
    person.full_name=full_name
    person.contact_address = contact_address
    person.email = email
    person.mobile = mobile
    person.save()
    return render(request, 'app9_1/display_person1.html', {'person': person})