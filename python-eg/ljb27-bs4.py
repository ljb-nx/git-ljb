# coding:utf-8

#导入bs4模块
from bs4 import BeautifulSoup
#做一个美味汤


soup = BeautifulSoup(open('ljbhtml.html',encoding='utf-8'),'html.parser')
#输出结果
#print(soup.prettify())

#找到的p的class属性值
print(soup.p['class'])
# u'title'
   
#找到a标签
print(soup.a)
# http://example.com/elsie" id="link1">Elsie
   
#找到所有的a标签
print(soup.find_all('a'))
# [http://example.com/elsie" id="link1">Elsie,
# http://example.com/lacie" id="link2">Lacie,
# http://example.com/tillie" id="link3">Tillie]
   
#找到id值等于3的a标签
print(soup.find(id="link1"))

#我们可以通过get_text 方法 快速得到源文件中的所有text内容。
print(soup.get_text())

#发现了没有，find_all方法返回的是一个可以迭代的列表
for link in soup.find_all('a'):
  print(link.get('href'))
