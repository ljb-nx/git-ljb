# -*- coding:utf-8 -*-
# re 正则表达式
# patter 正则表达式
# 用于替换的字符串
# string 要被替换的母字符串
# count 替换次数,默认为0表示无穷多次
# flags 标志位：是否区分大小写、是否多行匹配
# re.sub(pattern, repl, string, count=0, flags=0)
import re
# 单纯替换
text = '1+1=2'
res = re.sub(r'=',r'>',text,0,re.I)
print(text)
print(res)
print('------------0------------')
# 去除注释（无用信息、这在爬虫中往往用于数据清理）
text = '1+1=2 # 这是客观真理 \n' \
       ' 1+1>2 # 这是团结的力量 \n' \
       ' 1+1<2 # 这是内斗结果 \n'
res = re.sub(r'#.*$',r'',text,0,re.M)
print(text)
print('------------1----------')
print(res)
print('------------2----------')
res = re.sub(r'#.*$',r'',text,0,re.M)
print(res)
print('------------3----------')
res = re.sub(r'#.*$',r'',text,0,re.M|re.S)
print(res)
print('----------4------------')
res = re.sub(r'#.*$',r'',text,1,re.M)
print(res)
print('----------5------------')
res = re.sub(r'#.*$',r'',text,2,re.M) # 多行模式，去掉注释（替换）次数为 2
print(res)
print('----------6------------')
res = re.sub(r'#.*$',r'',text,3,re.M)
print(res)
print('----------7------------')
res = re.sub(r'#.*$',r'',text,2)# 不出标志说明是多行模式的话，$ 仅仅匹配末尾
print(res)
print('----------8------------')
res = re.sub(r'#.*$',r'',text,2,re.X)
print(res)
# 详细模式的多行将忽略空白字符和注释，故替换失败
# re.find（）查找默认对多行模式生效
print('----------9------------')
res = re.findall('#',text)
print(res)
