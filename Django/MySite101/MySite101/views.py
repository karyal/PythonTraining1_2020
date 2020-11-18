from django.http import HttpResponse
def index(request):
    return HttpResponse("<b>Welcome to the world of Django!!</b>")