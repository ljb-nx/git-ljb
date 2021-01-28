#/usr/bin/python
# coding:utf-8

'''def Fib(n):
    return 1 if n<=2 else Fib(n-1)+Fib(n-2)

k = int(input())

for i in range(1,k):
    print(Fib(i))


'''

target=int(input())
res=0
a,b=1,1
for i in range(target-1):
    a,b=b,a+b
    print(a)


