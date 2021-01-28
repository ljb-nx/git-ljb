# coding:utf-8

import time


print(time.localtime(time.time()))
print("=======================================")
print(time.strftime('%Y-%m-%d',time.localtime(time.time())))
print(time.strftime('%H:%M:%S',time.localtime(time.time())))
print(time.strftime('%H:%M',time.localtime(time.time())))
print("=======================================")
kk = time.strftime('%S',time.localtime(time.time()))
print(kk)

for i in range(4):
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    time.sleep(1)
