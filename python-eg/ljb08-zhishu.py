#!/usr/bin/python
# coding:utf-8
'''
===============================
ljb
判断一个数是质数。

===============================

'''


def zhishu(k):
    
    li = []
    for i in range(1,k+1):
        if (i == 1) :
            continue
        for j in range(1,i):
            yushu = i%j
            if (j == 1) :
                continue
            if yushu == 0 :
                #print i
                li.append(i)
                break
    num = 0 
    for m in range(1,k+1):
        if m not in li:
            print m ,
            num += 1
            if (num%10 == 0) :
                print ''
                num = 0



num1 = input("计算某个整数范围内的质数。请输入一个整数：")
zhishu(int(num1))
#zhishu(5)
