from django.shortcuts import render

# Create your views here.
def display_variables(request):
    full_name = "Raj Rai"
    contact_address="Kathmandu, Nepal"
    email_address="raj@gmail.com"
    context = {'name': full_name, 'address':contact_address, 'email': email_address}
    return render(request, "app5_1/Variables.html", context)

def display_tags(request):
    # autoescape
    # context = {'var_autoescape':'<p>You are <em>pretty</em> smart!</p>'}
    # return render(request, "Tags.html", context)

    #fruits = ['Apples', 'Bananas', 'Pears', 'Grapes', 'Oranges']
    #context={'fruits':fruits}
    # return render(request, "Tags.html", context)

    # extends, block
    # return render(request, 'app5_1/about.html')

    # firstof
    # context = {'var1':None, 'var2':None, 'var3':3}
    # return render(request, "Tags.html", context)

    # for
    # fruits = ['Apples', 'Bananas', 'Pears', 'Grapes', 'Oranges']
    # context = {'fruits': fruits}
    # return render(request, "Tags.html", context)

    # for...empty
    # fruits =[]
    # context={'fruits':fruits}
    # return render(request, "Tags.html", context)

    # if...endif
    # context={'sub1':45, 'sub2':54, 'sub3':78, 'PM':40}
    # return render(request, "app5_1/Tags.html", context)

    # include
    # return render(request, "app5_1/body.html")

    # load
    # return render(request, "app5_1/Tags.html")

    #regroup
    cities = [
        {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
        {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
        {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
        {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
        {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
    ]

    context = {'cities':cities}
    return render(request, "app5_1/Tags.html", context)

def display_filters(request):
    """
    full_name = "Raj Rai"
    contact_address="Kathmandu, Nepal"
    email_address=""
    context = {'name': full_name, 'address':contact_address, 'email': email_address}
    """
# add
    # val1 = [10, 39, 21]
    # val2 = [54, 22, 87]
    # context = {'val1': val1, 'val2':val2}
    # return render(request, "app5_1/Filters.html", context)

# addslashes
    # context = {'val1': "I can't."}
    # return render(request, "app5_1/Filters.html", context)

# capfirst
    # context = {'val1': "capitalizes the first character of the value."}
    # return render(request, "app5_1/Filters.html", context)

# center
    # context = {'val1': "Kathmandu"}
    # return render(request, "app5_1/Filters.html", context)

# cut
    # context = {'val1': "Removes all values of arg from the given string."}
    # return render(request, "app5_1/Filters.html", context)

# date time
    # import time
    # ts1 = time.time()

    # import datetime;
    # ts2 = datetime.datetime.now().timestamp()
    # ts2 = datetime.datetime.now()

    # import calendar;
    # import time;
    # ts3 = calendar.timegm(time.gmtime())

    # context = {'val1':ts2}
    # return render(request, "app5_1/Filters.html", context)

# default
    context = {'val1': None}
    context = {'val1': False}
    context = {'val1': 0}
    context = {'val1': ""}
    # return render(request, "app5_1/Filters.html", context)

# default_if_none
    context = {'val1': None}
    # return render(request, "app5_1/Filters.html", context)

# dictsort
    val1 = [
                {'name': 'Yadav', 'age': 25},
                {'name': 'Anuj', 'age': 22},
                {'name': 'Raj', 'age': 13},
            ]
    context = {'val1': val1}
    # return render(request, "app5_1/Filters.html", context)

# escape
    val1 = "<First's Page>"
    context = {'val1': val1}
    # return render(request, "app5_1/Filters.html", context)

# filesizeformat
    val1 = 1245788
    context = {'val1': val1}
    # return render(request, "app5_1/Filters.html", context)

# first
    val1 = ['Apples', 'Bananas', 'Pears', 'Grapes', 'Oranges']
    context = {'val1': val1}
    # return render(request, "app5_1/Filters.html", context)

# floatformat
    val1 ={'n1':123.456, 'n2':123.450, 'n3':123.001}
    context = {'val1': val1}
    #return render(request, "app5_1/Filters.html", context)

# force_escape
    val1 = "<First's Page>"
    context = {'val1': val1}
    # return render(request, "app5_1/Filters.html", context)

# get_digit
    val1 = 1235478
    context = {'val1': val1}
    # return render(request, "app5_1/Filters.html", context)

# iriencode
    val1 = "?id=1&name=Raj Rai"
    context = {'val1': val1}
    # return render(request, "app5_1/Filters.html", context)

# join
    val1 = ['Apples', 'Bananas', 'Pears', 'Grapes', 'Oranges']
    context = {'val1': val1}
    # return render(request, "app5_1/Filters.html", context)

# json_script
    val1 = {'hello': 'world'}
    context = {'val1': val1}
    # return render(request, "app5_1/Filters.html", context)

# json_script
    val1 = {'hello': 'world'}
    context = {'val1': val1}
    # return render(request, "app5_1/Filters.html", context)

# linebreaks
    val1 = ['Apples', 'Bananas', 'Pears', 'Grapes', 'Oranges']
    context = {'val1': val1}
    return render(request, "app5_1/Filters.html", context)