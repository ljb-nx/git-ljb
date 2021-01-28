# -*- coding:utf-8 -*-
# re 正则表达式
import re
# patter 正则表达式
# string 待匹配的母字符串
# flags 标志位：是否区分大小写、是否多行匹配

text = 'This is a student,named MY from SJTU University.'

# re.match(pattern, string, flags=0)
# 定死了必须从开头的首元素位置（索引为0）开始匹配
res = re.match('This',text)# 默认flag为0，完全匹配模式（严格大小写、字符配对）
# <re.Match object; span=(0, 4), match='This'>
print(res)
res = re.match('this',text)
# None
print(res)
res = re.match('this',text,re.I)# 置 flags 为 re.I后忽略大小写；爬虫数据清洗通常使用多行匹配且不区分大小写的匹配模式
# <re.Match object; span=(0, 4), match='This'>
print(res)
res = re.match('is',text) # None，re.match()非开头即是匹配得到也不能够配对
print(res)
res = re.match('(.*)is',text)
# "."匹配任意字符（默认为贪婪模式、尽可能多地匹配） + "*"匹配前一个字符0次或多次 = 若存在，则往前取任意多字符直到起始位置（全部取）
# <re.Match object; span=(0, 7), match='This is'>
print(res)
res = re.match('(.*) is',text)# ' is'往前全部取、包括正则表达式子串本身（贪婪、会尽可能多匹配），上一个是'is'往前全部取，两者运行结果一样
# <re.Match object; span=(0, 7), match='This is'>
print(res)
res = re.match('(.*) is ',text)# ' is '往前全部取（包括正则表达式子串本身、贪婪模式会尽可能多匹配）
# <re.Match object; span=(0, 8), match='This is '>
print(res)
res = re.match('(.*?)is',text)# ‘？'匹配前一个元素0次或1次，默认懒惰模式、尽可能少匹配、故不含包括正则表达式子串，此例子中即不含'is'
# <re.Match object; span=(0, 4), match='This'>
print(res)
res = re.match('(.*?) is',text)
# <re.Match object; span=(0, 5), match='This '># 注意区分这句与上一句，一个空格引起差异
print(res)
res = re.match('(.*?)is ',text)
# <re.Match object; span=(0, 7), match='This is'>
print(res)
res = re.match('(.*?) is ',text) # 由上述三句可知'?'懒惰模式无法舍弃空格
# <re.Match object; span=(0, 8), match='This is '>
print(res)
