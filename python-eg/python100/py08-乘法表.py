#/usr/bin/python
# coding:utf-8

#pint()不换行函数候加，

for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%2d  '%(i,j,i*j)),
        
    print('') #注意print('')与print()的区别
