#!usr/bin/python
# coding:utf-8

from car.car import Car
'''
class Car:
    price=10000
    def __init__(self,c):
        self.color = c
'''

car1 = Car("red")
car2 = Car("write")

print(car1.color,Car.price)

Car.price = 120000
Car.name = 'QQ'
car1.color = 'yellow'

print(car2.color,Car.price,Car.name)
