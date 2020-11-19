from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Welcome to the world of Django!!</h2>"
                        "<h4><a href='app1'>App1</a></h4>"
                        "<h4><a href='app2'>App2</a><h4>")