#!usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2020-2-1

@author: lenovo
'''

#print ("Hello world!你好，世界！")

# 创建一个学生类
class Student:
    number = 0
    def __init__(self,name,score):
        self.name = name
        self.score = score
        Student.number = Student.number + 1
    def show(self):
        print("Name: {}. Score: {}".format(self.name, self.score))        

student1 = Student("John", 100)
student2 = Student("Lucy", 99)
student1.show()
student2.show()

print(Student.number) # 打印2
print(student1.__class__.number) # 打印2

if __name__ == '__main__':
    pass
