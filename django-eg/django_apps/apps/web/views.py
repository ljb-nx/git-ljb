from django.shortcuts import render, HttpResponse
 
 
def home(request):
    return HttpResponse("成功home")
 
 
def news(request, nid):
    print(nid)
    page = request.GET.get("page")
    return HttpResponse("新闻news")
 
 
def article(request):
    nid = request.GET.get("nid")
    print(nid)
    return HttpResponse("文章article")

 
def getWebName(request):
    return HttpResponse("编程抗氧化——web")