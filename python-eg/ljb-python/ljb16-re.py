# -*- coding:utf-8 -*-
# re 正则表达式
import re

str = 'This is the last one'
res = re.match('(.*) is (.*?).*',str,re.M | re.I)
print(res)
res = re.match('(.*) is (.*?)(.*)',str,re.M | re.I)
print(res)
res = re.match('(.*) is (.*).*',str,re.M | re.I)
print(res)
res = re.match('(.*) is (.*)',str,re.M | re.I)
print(res)
# 以上四个运行结果同为 <re.Match object; span=(0, 20), match='This is the last one'>
res = re.match('(.*) is (.*?)',str,re.M | re.I)
print(res)
# <re.Match object; span=(0, 8), match='This is '>
# 由上可知，'.*'贪心匹配、元素有则取之
# 由上可知，'.*？'懒惰匹配、满足正则子串即可（注意：空格也要匹配）
# 数据清洗通常使用多行匹配 re.M 且不区分大小写 re.I 的匹配模式

text = "aAbBAABBCcCcDdDdcCdD"

print( re.match("a.*d",text,re.I))
# <re.Match object; span=(0, 20), match='aAbBAABBCcCcDdDdcCdD'>
print( re.match("a.*d",text))
# <re.Match object; span=(0, 19), match='aAbBAABBCcCcDdDdcCd'>
print( re.match("a.*?d",text))
# <re.Match object; span=(0, 14), match='aAbBAABBCcCcDd'>
print( re.match("a.*?d",text,re.I))
# <re.Match object; span=(0, 13), match='aAbBAABBCcCcD'>

print( re.match("a.*b",text,re.I))
print( re.match("a.*?b",text,re.I))
print( re.match("a.*?B",text),re.I)
print( re.match("a.*?B",text))
print( re.match("a.*?b",text))
# 上边四句的输出结果依次对应如下：
# <re.Match object; span=(0, 8), match='aAbBAABB'>
# <re.Match object; span=(0, 3), match='aAb'>
# <re.Match object; span=(0, 4), match='aAbB'> RegexFlag.IGNORECASE
# <re.Match object; span=(0, 4), match='aAbB'>
# <re.Match object; span=(0, 3), match='aAb'>

