# -*- coding:utf-8 -*-
# re 正则表达式
# findall(string[, pos[, endpos]])
import re

res = re.findall(r"\d", "图书馆2019年11月的阅读次数为 99万")  # 返回的是不可修改的元组
print(res) # ['2', '0', '1', '9', '1', '1', '9', '9']
res = re.findall(r"(\d+)", "图书馆2019年11月的阅读次数为 99万，点赞数：3200")
print(res)  # ['2019', '11', '99', '3200']
res = re.findall(r"(\D+)", "图书馆2019年11月的阅读次数为 99万，点赞数：3200")
print(res)  # ['图书馆', '年', '月的阅读次数为 ', '万，点赞数：']
for i in res:
    print(i)

print('--------分割线---------')
# words = ['wooves','Tools','food','too','cool','hello','zoo']
words = 'wooves Tools food too cool hello zoo \n goods'
print("1 ",re.findall(r'Oo',words))
print('2 ',re.findall(r'Oo',words,re.I))
print('3 ',re.findall(r'(\w+)(Oo)(\w*)',words,re.I))
    # 方式3 正则表达式全部被括号分割包围时，结果为元组内部嵌套了列表
    # 方式4 将按照元祖形式输出符合匹配条件的“单词”（即含有元素“oo”、不区分大小写）
print('4 ',re.findall(r'\w+Oo\w*',words,re.I))
print('5 ',re.findall(r'\w+(Oo\w*)',words,re.I))
    # 当正则表达式只是部分还有括号时，仅输出 括号部分对应的元祖（字符串）
print('6 ',re.findall(r'(\wOo)w*',words,re.I))
print('7 ',re.findall(r'(\wOo).*',words,re.I))
print('8 ',re.findall(r'(\wOo)(.*)',words,re.I))
print('9 ',re.findall(r'\wOo.*',words,re.I))
print('10 ',re.findall(r'\w+oo\w.*',words))
print('11 ',re.findall(r'\w+oo\w.*',words,re.S))
    # re.S 模式下 '.'可以匹配任意字符，包括默认不允许的回车‘\n’换行符
