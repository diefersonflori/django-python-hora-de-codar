from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def helloworld(request):
    return HttpResponse('Hello World!')

def tasklist(request):
    return render(request,'tasks/list.html')

def yourName(request,name):
    return render(request,'tasks/yourname.html',{'name':name})
    