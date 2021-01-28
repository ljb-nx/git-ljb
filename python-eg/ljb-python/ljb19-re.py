# -*- coding:utf-8 -*-
# re 正则表达式
# patter 正则表达式(定义字符串如何构成）
# flags 标志位：是否区分大小写、是否多行匹配
# re.compile(pattern[, flags])
import re
words = 'woo2345ves Too_ls food too cool hello zoo \n goods'
ret = re.compile(r'\w*oo\w*') # 编译生成查找含有oo字母元素的单词的正则表达模式对象 obj对象可以直接调用re的方法
print(re.findall(ret,words)) # re.findall() 默认多行查找
print((ret.findall(words))) # 这是第二种有效的等价写法
# 正则模式的对象obj可以直接调用re的任何方法
