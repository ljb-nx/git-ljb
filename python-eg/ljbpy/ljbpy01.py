#!usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2020��2��1��

@author: lenovo
'''

#print ("Hello world!你好，世界！")

# 创建一个学生类
class Student:

    # number属于类变量，不属于某个具体的学生实例
    number = 0

    # 定义学生属性，初始化方法
    # name和score属于实例变量
    def __init__(self,name,score):
        self.name = name
        self.score = score
        Student.number = Student.number + 1

    def show(self):
        #print("Name: {}. Score: {}".format(self.name, self.score))
        print("Name: %s. Score: %.2f" %(self.name, self.score))
       

# 实例化，创建对象
student1 = Student("John", 100)
student2 = Student("Lucy", 99)

student1.show()
student2.show()
print(Student.number)
print(student1.__class__.number) # 打印2

if __name__ == '__main__':
    pass