#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time:2021/7/27 22:37
# Description:

# a = 1
#
#
# def demo1():
#     global a
#     a=2
#     print(a)
#     print(id(a))
#
#
# demo1()
# print(id(a))

def outer():
    def inner():
        print("inner")
        return "hahahha"
    return inner


print(outer()())