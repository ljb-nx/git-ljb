#!/usr/bin/python
# coding:utf-8
'''
不用if-else的简单计算器算法。经典。
ljb。
'''
from operator import *

def calculator(a, b, k):
    return {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv,
        '**': pow   }[k](a, b)

print calculator(1, 2, '+') 
print calculator(3, 4, '**')
