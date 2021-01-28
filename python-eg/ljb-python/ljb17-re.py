# -*- coding:utf-8 -*-
import re
text = 'This is a text written by MY ,' \
       'from SheHui University on 2019/11/06 at 00:39.'

print(text)
res = re.search(r'(\d)',text,re.I)
# <re.Match object; span=(69, 70), match='2'>
# \d 同 [0-9] 匹配任意（单个）十进制数
print(res)
res = re.search(r'(\D)',text,re.I|re.M)
# <re.Match object; span=(0, 1), match='T'>
# \D 同 [^0-9] 匹配任意（单个）非数字字符
# 注意：符号^在方括号内
print(res)

res = re.search(r'(\d).*',text,re.I|re.M)
# <re.Match object; span=(69, 89), match='2019/11/06 at 00:39.'>
print(res)
res = re.search(r'.* (\d)',text,re.I)
print(res)
res = re.search(r'.*(\D).*',text,re.I)
print(res)
res = re.search(r'.*(\D)',text,re.I)
print(res)

res = re.search(r'(\D).*',text,re.I|re.M)
# 上边被注释掉的3句，运行结果与此句相同
# <re.Match object; span=(0, 88), match='This is a text written by a student named MY from>
print(res)

