#!/usr/bin/python
# coding:utf-8
'''
题目 判断101-200之间有多少个素数，并输出所有素数。
'''

import math

for i in range(100,200):
    flag=0
    kk = '{:.0f}'.format(round(math.sqrt(i))+1)



    for j in range(2,int(kk)):
        if i%j==0:
            flag=1
            break
    if flag:
        continue
    print(i)

