#!/usr/bin/python3
# coding:utf-8

num = [ n1*10+n2 for n1 in range(0, 10)
            for n2 in range(0, 10) if n1 == n2+1 ]

print(num)
