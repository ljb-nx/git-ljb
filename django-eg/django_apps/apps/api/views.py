from django.shortcuts import render,HttpResponse
# Create your views here.
 
def getApiName(request):
    return HttpResponse("编程抗氧化——api")