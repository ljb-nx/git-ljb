#/usr/bin/python
# coding:utf-8

def factor(num):
    target=int(num)
    res=set() #集合元素不允许重复
    for i in range(1,num):
        if num%i==0:
            res.add(i)
            res.add(num/i)
    return res

for i in range(2,100):
#注意sum函数的使用
    if i==sum(factor(i))-i:
        print(i)
