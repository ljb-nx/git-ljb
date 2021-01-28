#!/usr/bin/python
# coding:utf-8
'''
===============================
ljb
return语句返回字典的例子。经典。

===============================

'''
def func1():
    parameters = {'a':1,'b':2,'c':3}
    return parameters

def func2(k):
    return{'a':1,'b':2,'c':3}[k]


print func1()['a']

#用简洁方式返回
print func2('a')

func2('a')

