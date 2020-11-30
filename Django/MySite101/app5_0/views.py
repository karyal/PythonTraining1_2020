from django.shortcuts import render
# Create your views here.

def filters(request):
    return render(request, 'app5_0/Filters.html')

def tags(request):
    # var1 = "Kathmandu"
    # context = {'value1': var1}
              # key : value
    # return render(request,  'app5_0/Tags.html', context)

    # autoescape
    # var1 = "<b>Hello</b>"
    #context = {'value': var1}
    #return render(request,  'app5_0/Tags.html', context)

    # cycle
    fruits = ['Apples', 'Bananas', 'Pears', 'Grapes', 'Oranges']
    context = {'value': fruits}
    return render(request,  'app5_0/Tags.html', context)