#!/usr/bin/python
# coding:utf-8

def lifang(n):
    m = n**3
    return m
    
k = input("输入一个数:")
# str1 = str(k)

k = int(k)
i = 1
j = 0
sum = 0

for i in range(1,k + 1):
    for j in range(len(str(i))):
        sum = sum + lifang(int(str(i)[j]))
#    print i,sum

    if (i == sum):
        print(i, sum)
    sum = 0
