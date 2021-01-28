# coding:utf-8

list_eg = [70, 45, 37, 127, 148, 26, 121]
sorted_eg = sorted(list_eg, key=lambda x: x)	# 这里不加lambda函数也是返回一样的结果
print(sorted_eg)	# [26, 37, 45, 70, 121, 127, 148]

print('==================================')
sorted_eg0 = sorted(list_eg)	# 这里不加lambda函数也是返回一样的结果
print(sorted_eg0)	# [26, 37, 45, 70, 121, 127, 148]

print('==================================')
sorted_eg1 = sorted(list_eg, key=lambda x: x,reverse=True)	# 添加reverse=True，为倒序输出
print(sorted_eg1)
