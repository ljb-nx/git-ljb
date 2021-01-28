# coding:utf-8

# 字串分割
str = "ABCDABCDABCD"
print( str.split('A'))# 返回元组（元组的元素不可更改）
print( str.split('A',2))# 分割成 i+1份（i为数字参数）在最左边分割，左侧将会产生空串
print( str.split('B',2))# 分割成 i+1份（i为数字参数），分割时去除分隔符
print( str.split('D',2))# 在最右边元素产生分割无效，有且仅有此种情况保留分隔符

# 字串的分割和替换是数据清洗的基本
