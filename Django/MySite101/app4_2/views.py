from django.shortcuts import render

# Create your views here.
def template_1(request):
    return render(request, "app4_2/Template1.html")

def template_2(request):
    return render(request, "app4_2/Template2.html")

def template_3(request):
    return render(request, "app4_2/Template3.html")