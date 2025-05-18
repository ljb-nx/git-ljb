from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

# 用户信息
class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)


# 出版社表
class Publisher(models.Model):
    name = models.CharField(max_length=254)

# 图书表  图书属于一个出版社，一个出版社可以有多本书，一对多的关系
class Book(models.Model):
    name = models.CharField(max_length=64)
    publisher = models.ForeignKey(to=Publisher,on_delete=models.CASCADE) # 在django中创建外键
    # book_version = models.CharField(max_length=20,)   # 版本
    # book_price = models.CharField(max_length=20)  # 价格
    # book_number = models.IntegerField()  # 总库存数(馆藏数）
    # book_rest = models.IntegerField()  # 可借数
    # book_place = models.CharField(max_length=20)  # 所属书库
   

# 作者表
class Author(models.Model):
    name = models.CharField(max_length=64)
    # 一个作者可以对应多本书，一本书可以有多个作者，多对多
    # 在数据库中 自动创建第四张表 ：author_book
    book = models.ManyToManyField(to=Book)

