#!/usr/bin/python
# coding:utf-8

# 简单foreach循环，需要Python3
def foreach(function, iterator):
    for item in iterator:
        function(item)
    return
def printItself(it):
    print(it,end=" ")
    return
# 在这里，试着比较直接使用print与使用printItself的效果

my_tuple = (1, 2, 3, [4, 5], 6)
my_dictionary = {"Apple": "Red",
                 "Banana": "Yellow",
                 "Pear": "Green"
             }
foreach(printItself, my_tuple)
    # 1 2 3 [4, 5] 6 #注释行为对应的输出结果，下同
print('\n')
print(my_tuple)

foreach(print, my_tuple)
    # 1
    # 2
    # 3
    # [4, 5]
    # 6
foreach(print, range(len(my_tuple)))
    # 0
    # 1
    # 2
    # 3
    # 4
print()

foreach(print, my_dictionary)
foreach(print, my_dictionary.keys())
    # 上二个语句等价，输出相同
    # Apple
    # Banana
    # Pear
foreach(print, my_dictionary.values())
    # Red
    # Yellow
    # Green
print()

print(my_dictionary)
    # {'Apple': 'Red', 'Banana': 'Yellow', 'Pear': 'Green'}
print(my_dictionary.keys())
    # dict_keys(['Apple', 'Banana', 'Pear'])
print(my_dictionary.values())
    # dict_values(['Red', 'Yellow', 'Green'])
print()

foreach(printItself, range(len(my_dictionary)))
    # 0 1 2
print()
foreach(printItself,my_dictionary.keys())
    # Apple Banana Pear
print()
foreach(printItself,my_dictionary.values())
    # Red Yellow Green
print("\n")

foreach(print,my_dictionary)
print()
foreach(print,my_dictionary.keys())
    # 上二个语句等价，输出相同
    # Apple
    # Banana
    # Pear
print()
