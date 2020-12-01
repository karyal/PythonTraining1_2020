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
    # fruits = ['Apples', 'Bananas', 'Pears', 'Grapes', 'Oranges']
    # context = {'value': fruits}
    # return render(request,  'app5_0/Tags.html', context)

    # extends | block
    #page_title ="Page Title-1"
    #heading = "Title-1"
    #content = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    #context = {'page_title': page_title, 'body_title': heading, 'body_text' : content}
    #return render(request,  'app5_0/about.html', context)

    # firstof
    #context = {'var1':None, 'var2':None, 'var3':3}
    #return render(request, 'app5_0/Tags.html', context)

    # filter
    # context = {'var1':'<b>Lorem Ipsum Is simplY Dummy teXt of tHe printinG</b>'}
    # return render(request, 'app5_0/Tags.html', context)

    #for loop
    #fruits = ['Apples', 'Bananas', 'Pears', 'Grapes', 'Oranges']
    #context = {'fruits': fruits}
    #return render(request, 'app5_0/Tags.html', context)

    # if statment
    #context = {'sub1':56, 'sub2':87, 'sub3':54, 'sub4':90, 'PM':40}
    #return render(request, 'app5_0/Tags.html', context)

    # include
    # return render(request, 'app5_0/body.html')

    # load
    # pip install humanize
    return render(request, 'app5_0/Tags.html')