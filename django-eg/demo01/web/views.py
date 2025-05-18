# Create your views here.
from django.shortcuts import render, HttpResponse
 
 
def info(request):
    print('请求执行来了')
    return HttpResponse("info")
 
 
def xxxx(request):
    print('请求执行来了')
    return HttpResponse("。。。。。。xxxx。。。。。。")
 
 
