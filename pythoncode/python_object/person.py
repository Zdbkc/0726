#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time:2021/8/3 7:03
# Description:

class Person:
    # name = 'name'
    # gender = '男'
    # age = 18
    # 私有属性
    __money = 500

    # 构造方法
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

    def run(self):
        print(f'{self.name} is running')

    def have_money(self):
        print(f'{self.name} has money {self.__money} ')
        print(f"现在的money是：{self.__get_money()}")

    # 私有方法
    def __get_money(self):
        return self.__money + 1000

    # 类方法
    @classmethod
    def some_method(cls):
        print(f"这是类方法")


class Funny(Person):
    # 继承 Person 类的属性和方法
    # 新增方法 fun() 搞笑 方法

    def __init__(self, name, gender, age, skill):
        super().__init__(name, gender, age)
        self.skill = skill

    def fun(self):
        print(f'{self.name} is funny')



fun1 = Funny('法外的狂徒张三', '男', 26, '表演')
print(fun1.name, fun1.gender, fun1.age, fun1.skill)
fun1.run()
fun1.fun()
print(fun1.have_money())

Funny.some_method()
Person.some_method()
# Funny.fun()

# p1 = Person('法外狂徒张三', '男', 25)
# print(p1.name, p1.gender, p1.age)
# p1.eat()
# p1.sleep()
# p1.run()
# p1.have_money()
# print(dir(p1))
