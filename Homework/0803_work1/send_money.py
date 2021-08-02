#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time:2021/8/3 5:12
# Description:
import money


def send_money(add_money):
    print(f"现有存款为：{money.saved_money}")
    money.saved_money += add_money
    print("发工资了")
