from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def getvalue_1(request):
    # get value
    full_name = request.GET.get('full_name')
    # print(full_name)
    context = {'name': full_name}
    return render(request, 'app4_3/File1.html', context)

def getvalue_2(request, full_name, address):
    #print(full_name)
    context = {'name': full_name, 'address': address}
    return render(request, 'app4_3/File2.html', context)

def display_form1(request):
    return render(request, 'app4_3/Form1.html')

def display_form2(request):
    return render(request, 'app4_3/Form2.html')

def getvalue_3(request):
    if request.method=='GET':
        name = request.GET.get('txt_name')
        context = {'name':name}
        return render(request, 'app4_3/File3.html', context)
    elif request.method == 'POST':
        name = request.POST.get('txt_name')
        context = {'name': name}
        return render(request, 'app4_3/File3.html', context)