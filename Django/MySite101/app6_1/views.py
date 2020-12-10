from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import app6_1.my_module as module

# Create your views here.
def index(request):
    persons = module.select_all()
    context = {'persons': persons}
    return render(request, 'app6_1/index.html', context)

def new(request):
    return render(request, 'app6_1/add_new.html')

def insert(request):
    if request.method == 'GET':
        p1 = module.person(request.GET.get('txt_id'), request.GET.get('txt_name'), request.GET.get('txt_address'))
    else:
        p1 = module.person(request.POST.get('txt_id'), request.POST.get('txt_name'), request.POST.get('txt_address'))
    result = module.insert(p1)
    return HttpResponseRedirect("..")

def edit(request):
    pid = request.GET.get('pid')
    p1 = module.search(pid)
    print(p1)
    return render(request, 'app6_1/edit.html',{'person': p1})

def update(request):
    p1 = module.person(request.POST.get('txt_id'), request.POST.get('txt_name'), request.POST.get('txt_address'))
    result = module.update(p1)
    return HttpResponseRedirect("..")

def display_delete(request):
    pid = request.GET.get('pid')
    p1 = module.search(pid)
    print(p1)
    return render(request, 'app6_1/delete.html',{'person': p1})

def delete(request):
    pid = request.POST.get('txt_id')
    print(pid)
    result = module.delete(pid)
    return HttpResponseRedirect("..")