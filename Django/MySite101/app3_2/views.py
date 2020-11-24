from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    n1 = request.GET.get('num1')
    n2 = request.GET.get('num2')
    n3 = int(n1)+int(n2)
    return HttpResponse("Num1 : "+str(n1)+"<br/>"
                        "Num2 : "+str(n2)+"<br/>"
                        "Result : "+str(n3)+"<br/>"
                        )

def calculate(request):
    n1 = request.GET.get('num1')
    n2 = request.GET.get('num2')
    operator = request.GET.get('opr')
    print(operator)

    if operator=='.':
        n3 = float(n1) + float(n2)
        operator='+'
    elif operator=='-':
        n3 = float(n1) - float(n2)
    elif operator=='*':
        n3 = float(n1) * float(n2)
    elif operator=='/':
        n3 = float(n1) / float(n2)
    else:
        n3 = 'NA'
    context = {'num1': n1, 'num2': n2, 'oper': operator, 'num3': n3}
    return render(request, "Calculator.html", context)

    # return HttpResponse("Num1 : " + str(n1) + "<br/>Num2 : " + str(n2) + "<br/>Operator : " + str(operator) + "<br/>Result : " + str(n3) + "<br/>")