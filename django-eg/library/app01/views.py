from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponse,redirect
from app01 import models

# Create your views here.

user_info = False

# 注册
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        models.User.objects.create(username=username,password=password)
        return redirect('/login/')
    return render(request,'register.html')


# 登录
def login(request):
    login_status = ''
    global user_info
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = models.User.objects.filter(username=username)
        if not user_obj:
            return HttpResponse('没有此用户')
        if password == user_obj[0].password:
            user_info = True
            return redirect('/book_list/')
        else:
            return HttpResponse('密码错误')

    return render(request,'login.html')



# 出版社视图函数
def publisher_list(request):
    if not user_info:
        return redirect('/login/')
    # 查询全部的记录
    publisher_list = models.Publisher.objects.all()
    # 渲染到前端页面
    return render(request,"publisher_list.html",{'publisher_list':publisher_list})

# 新增出版社
def add_publisher(request):
    if not user_info:
        return redirect('/login/')
    if request.method == "POST":
        publisher_name = request.POST.get('publisher_name')
        models.Publisher.objects.create(name=publisher_name)
        return redirect('/publisher_list/')
    return render(request,'add_publisher.html')

# 编辑出版社
def edit_publisher(request):
    if not user_info:
        return redirect('/login/')
    id = request.GET.get("id")
    plisher_obj = models.Publisher.objects.filter(id=id)

    if request.method == "POST":
        publisher_name = request.POST.get("publisher_name")
        models.Publisher.objects.filter(id=id).update(name=publisher_name)
        return redirect('/publisher_list/')
    return render(request,'edit_publisher.html',{"plisher_obj":plisher_obj[0]})

# 删除出版社
def del_publisher(request):
    id = request.GET.get("id")
    models.Publisher.objects.filter(id=id).delete()
    return redirect('/publisher_list/')

# 图书列表
def book_list(request):
    if not user_info:
        return redirect('/login/')
    
    book_page_num = int(request.GET.get('page_num', 1))  # 用户不传页码默认为1
    book_list = models.Book.objects.all()  # 获取所有数据
    
    '''Paginator 对象'''
    # 实例化
    paginator = Paginator(book_list, 5)  # 分页的数据，每页显示十行
    # print(paginator.count)  # 总条数   500
    # print(paginator.num_pages)   # 总页数 50
    # print(paginator.per_page)  # 每页显示条数 10
    # print(paginator.page_range) # 生成器，next拿一页  range(1,51)
    # print(paginator.page(1))  # page(1)第一页，()内写几可以拿到的页
    # 判断页码数和11的关系，布局

    '''Page对象'''
    try:
        page = paginator.page(book_page_num)  # 获取当前页
        # print(page.has_next())  # 判断有没有下一页  True
        # print(page.next_page_number())  # 下一页页码数  3
        # print(page.has_previous())  # 判断有没有上一页 True
        # print(page.previous_page_number())  # 上一页页码 1
        # print(paginator.object_list)   # 获取该页的所有数据的对象
    except Exception as e:
        book_page_num = paginator.num_pages  # 如果没有搜索页设置默认数显示最后一页
        page = paginator.page(book_page_num)  # 没有搜索页显示最后一页
    # print(page.number)   # 获取当前页码 2

    if paginator.num_pages > 11:
        # 开头的判断，如果当前页-5小于1，那么显示1，12
        if book_page_num - 5 < 1:
            page_range = range(1, 12)
        # 末尾的判断，如果当前页+5大于总页码数，回退11
        elif book_page_num + 5 > paginator.num_pages:
            page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
        # 中间当前页-5，+6
        else:
            page_range = range(book_page_num - 5, book_page_num + 6)
    else:
        page_range = paginator.page_range  # 如果小于11那么就显示少有的对象



    # book_list = models.Book.objects.all()
    return render(request,'book_list.html',locals())

# 新增图书
def add_book(request):
    if not user_info:
        return redirect('/login/')
    publisher_list = models.Publisher.objects.all()
   
    author_list = models.Author.objects.all()

    if request.method == "POST":
        book_name = request.POST.get("book_name")
        publisher_id = request.POST.get("publisher_id")
        # author_id = request.POST.get("author_id")


        models.Book.objects.create(name=book_name,publisher_id=publisher_id)
        # book_obj = models.Book.objects.first()
        # print(book_obj)
        return redirect('/book_list/')
    return render(request,'add_book.html',{"publisher_list":publisher_list,"author_list":author_list})

# 编辑图书
def edit_book(request):
    if not user_info:
        return redirect('/login/')
    book_id = request.GET.get("book_id")
    book_obj = models.Book.objects.filter(id=book_id)
    # book_name = book_obj[0].name
    publisher_list = models.Publisher.objects.all()

    if request.method == "POST":
        book_name = request.POST.get("book_name")
        publisher_id = request.POST.get("publisher_id")
        models.Book.objects.filter(id=book_id).update(name=book_name,publisher_id=publisher_id)
        return redirect('/book_list/')
    return render(request,'edit_book.html',{"book_obj":book_obj[0],"publisher_list":publisher_list})

# 删除图书
def del_book(request):
    if not user_info:
        return redirect('/login/')
    book_id = request.GET.get("book_id")
    models.Book.objects.filter(id=book_id).delete()
    return redirect('/book_list/')


# 作者列表
def author_list(request):
    if not user_info:
        return redirect('/login/')
    author_list = models.Author.objects.all()
    return render(request,'author_list.html',{"author_list":author_list})

# 新增作者
def add_author(request):
    if not user_info:
        return redirect('/login/')
    # book_list = models.Book.objects.all()
    if request.method == "POST":
        author_name = request.POST.get("author_name")
        models.Author.objects.create(name=author_name)
        return redirect('/author_list/')
    return render(request,'add_author.html')

# 编辑作者
def edit_author(request):
    if not user_info:
        return redirect('/login/')
    author_id = request.GET.get("author_id")
    author_obj = models.Author.objects.filter(id=author_id)
    book_list = models.Book.objects.all()

    if request.method == "POST":
        author_name = request.POST.get("author_name")
        book_id = request.POST.getlist("book_id")
        author_obj[0].name = author_name
        author_obj[0].book.set(book_id)
        author_obj[0].save()

        # models.Author.objects.filter(id=author_id).update(name=author_name)
        return redirect('/author_list/')
    return render(request,'edit_author.html',{"author_obj":author_obj[0],"book_list":book_list})


# 删除作者
def del_author(request):
    if not user_info:
        return redirect('/login/')
    author_id = request.GET.get("author_id")
    models.Author.objects.filter(id=author_id).delete()
    return redirect('/author_list/')
