#!/usr/bin/python
# coding:utf-8
from __builtin__ import str

def jiechen(n):
    #n的阶乘
    if n == 1:
        cj = 1
    else:
        cj = n * jiechen(n - 1)
        
    return cj

i = 1
try:
    m = input("请输入一个整数，计算这个整数的阶乘：")
except:
    print "输入的数不是一个整数。"
    exit()

for i in range(1,m + 1):
    print "这个数%d! = %d:" %(i,jiechen(i))
    
# print "这个数%d! = %d:" %(m,jiechen(m))