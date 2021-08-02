#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time:2021/8/2 20:45
# Description:
# from pythoncode.gift import have_gift
import gift

def show_gift():
    have_gift=gift.have_gift
    if have_gift is True:
        print("收到礼物了，很开心")
    else:
        print("等待礼物中")