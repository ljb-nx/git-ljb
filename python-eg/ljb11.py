# -*- coding: UTF-8 -*-
# 范式编程（函数式编程）

def main():
    my_dict = {'子': '鼠', '丑': '牛', '寅': '虎', '卯': '兔',
               '辰': '龙', '巳': '蛇', '午': '马', '未': '羊',
               '申': '猴', '酉': '鸡', '戌': '狗', '亥': '猪'}
    prinfDictKeys(my_dict)
    printDictValues(my_dict)
    printDict(my_dict)

def prinfDictKeys(dict):
    for key in dict.keys():
        print(key, end=" ")
    print()

def printDictValues(dict):
    for value in dict.values():
        print(value, end=" ")
    print()

def printDict(dict):
    for key in dict:
        print(key,":",dict[key],end='\t\t')

if __name__ == '__main__':
    main()
