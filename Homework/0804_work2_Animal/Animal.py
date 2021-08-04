#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time:2021/8/4 7:21
# Description:
import yaml


class Animal:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def bark(self):
        print(f"{self.name} 能 叫")

    def run(self):
        print(f"{self.name} 能 跑")


class Cat(Animal):
    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)
        self.hair = "短发"

    def catch_mouse(self):
        print(f"捉到了老鼠")

    def bark(self):
        print(f"喵喵叫")


class Dog(Animal):
    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)
        self.hair = "长发"

    def watch_home(self):
        print(f"在看家")

    def bark(self):
        print(f"汪汪叫")


# with open("./data.yaml", mode='r', encoding='utf-8') as f:
#     datas = yaml.safe_load(f)
# print(datas)

with open("./data.yaml", encoding="utf-8") as f:
    data = yaml.safe_load(f)
    # 可以通过改变yaml中default的引用，来改变所选择的猫和狗
    data_test = data["default"]
    choose_cat = data_test["cat"]
    choose_dog = data_test["dog"]
    print(data_test)
    print(choose_cat)
    print(choose_dog)

if __name__ == '__main__':
    cat1 = Cat('喵喵1', '橘黄色', 2, '雄性')
    print(cat1.name, cat1.color, cat1.age, cat1.gender, cat1.hair, end=' ')
    cat1.catch_mouse()
    dog1 = Dog('汪星人1', "黑色", 3, '雌性')
    print(dog1.name, dog1.color, dog1.age, dog1.gender, dog1.hair, end=' ')
    dog1.watch_home()
