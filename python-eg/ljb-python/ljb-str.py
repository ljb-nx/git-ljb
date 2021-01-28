#!/usr/bin/python
# coding:gbk

# 打开文件
try:
    fo = open("C语言经典程序100例.txt", "r+")
except IOError:
    print "注意：没有此文件。"
print "文件名为: ", fo.name

str1 = fo.read()
# print "读取的字符串: %s" % (str1)

y_len = len(str1) #str1串长度
i = 0
start_str = "【"  #起始串
end_str = "程序分析"  #终止串

'''
print start_str,end_str

char1 = str1[i:i+2]
print char1
'''

#fo1 = open("python语言程序.txt", "a+")

for i in range(0,y_len):
    char1 = str1[i:i+2]
    
    if (char1 == start_str):
        start_weizhi = str1.find(start_str,i)
        end_weizhi = str1.find(end_str,start_weizhi + 2)
        print str1[start_weizhi:end_weizhi - 2]
        #fo1.write(str1[start_weizhi:end_weizhi - 2] + "\n")
        
        continue

# 关闭文件
fo.close()
#fo1.close()

