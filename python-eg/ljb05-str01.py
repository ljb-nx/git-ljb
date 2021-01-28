#!/usr/bin/python
# coding:gbk

# 打开文件
fo = open("C语言经典程序100例一.txt", "r+")
print "文件名为: ", fo.name

str1 = fo.read()
# print "读取的字符串: %s" % (str1)

y_len = len(str1)
i = 0
start_str = "【"
end_str = "1.程序分析"

for i in range(0,y_len):
    char1 = str1[i,i+1]
    print char1
    
# 关闭文件
fo.close()
