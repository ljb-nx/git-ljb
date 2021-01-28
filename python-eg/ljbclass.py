#!/usr/bin/python
# -*- coding: utf-8 -*-

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

