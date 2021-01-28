# -*- coding:utf-8 -*-
# re 正则表达式
# patter 正则表达式（用于替换的字符串）
# string 作为分隔素材的母字符串
# maxsplit 用于指定最大分割次数，不指定则默认为0表示无穷大、将全部分割
# flags 标志位：是否区分大小写、是否多行匹配
# re.split(pattern, string[, maxsplit=0, flags=0])
# 返回列表

import re
words = 'woov es Tools food too cool hello zoo \n goods'
res = re.split(r'\W',words)
print(res)
res = re.split(r'\s',words)
print(res)
res = re.split(r'\s+',words) # 这才是正确去除所有空白符 [\t\n\r\f\v] 因为 *与+ 表示贪心模式(?要看情况）
print(res)
res[1]='123' # 成功修改，故返回的是列表而不是元组
print(res)

text = '?a_b!2@'
res = re.split(r'\w+',text) # 由该句可知：\w除了匹配字母和数字，还匹配下划线（标识符命名规则……）
print(res)

print(re.split('a','1A1a2A3',re.I)) # ['1A1', '2A3']
print(re.split('a','1A1a2A3',0,re.I))# ['1', '1', '2', '3']
# 请注意使用格式这个大坑，否则将会导致re.I无法忽略字母的大小写
