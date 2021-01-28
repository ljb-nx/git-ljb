# -*- coding:utf-8 -*-
import re
# re.escape(string)
# string 为需要转义的字符串（常作为正则表达字串）
str = 'www.12306.cn \n' \
      'www.baidu.com '
pat = '\w+.*'
ret = re.escape(pat)
print( pat)
print( ret)
# findall(pattern, string, flags=0)
print( re.findall(pat,str))
print( re.findall(ret,str))
print( re.findall(r'\w+w..*',str))
print( re.findall(r'(\w+)(w.)(.*)',str))
# 输出依次为
# \w+w..*
# \\w\+w\.\.\*
# ['www.12306.cn ', 'www.baidu.com ']
# []
# ['www.12306.cn ', 'www.baidu.com ']
# [('ww', 'w.', '12306.cn '), ('ww', 'w.', 'baidu.com ')]
# escape “逃离”->“偏离原有意图”
# 不再是 raw string 原生字符串、可以可以表示转义
# 而是 硬生生的字符本身、别无组合之后的其他意思
