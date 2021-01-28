# coding:utf-8

# 直接通过迭代器遍历元素
py = "python"
for character in py:
    print(character)

print()#默认会输出空行

# 通过列表的索引遍历元素
for i in range(len(py)):
    print(i,py[i])

print("\nlen(py)=",len(py))
