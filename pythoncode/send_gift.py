#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time:2021/7/31 17:37
# Description:

# have_gift = ""
#
#
# def send_gift():
#     gift = input("请输入需要发的礼物：")
#     global have_gift
#     have_gift = gift
#
#
# def display_gift():
#     global have_gift
#     print(f"这是我收到的礼物：{have_gift}")
#
# send_gift()
# display_gift()

# have_gift = False

# from gift import have_gift
"""
浅拷贝：就是只拷贝第一层，如果里面有嵌套，不会改变
深拷贝：完全跟之前的内容没有任何关系，原来的对象怎么变，都不影响当前的对象（断开的关系）

from import 相当于深拷贝，相当于完全复制了一份内存地址
import 相当于浅拷贝，引用了模块的地址
"""


import gift
def send_gift():
    # global have_gift
    choice = input("请选择是否发礼物 “是” 或者 “否”：")
    if choice == "是":
        gift.have_gift = True
    else:
        gift.have_gift = False
    print("发礼物了")


