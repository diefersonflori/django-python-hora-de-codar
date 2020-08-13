from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def tasklist(request):
    tasks= Task.objects.all()
    return render(request,'tasks/list.html',{'tasks':tasks}) #o valor dela sao as tasks que eu resgatei do banco

def helloworld(request):
    return HttpResponse('Hello World!')


def yourName(request,name):
    return render(request,'tasks/yourname.html',{'name':name})
    