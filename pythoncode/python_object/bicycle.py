#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time:2021/8/3 7:51
# Description:

class Bicycle:

    def run(self, km):
        # self.km = km
        print(f"需要骑行{km}公里")


class EBicycle(Bicycle):
    battery_level: int = 0

    def __init__(self, battery):
        self.battery_level = battery

    def fill_charge(self, vol):
        self.battery_level += vol

    def run(self, km):
        last = km - self.battery_level * 10
        if last > 0:
            print("电不够用")
            print(f"使用电骑行{self.battery_level * 10}公里")
            super().run(last)
        else:
            print("电够用")
            print(f"使用电骑行{km}公里")


if __name__ == '__main__':
    e1 = EBicycle(10)
    e1.fill_charge(10)
    e1.run(201)
