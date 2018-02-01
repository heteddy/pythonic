# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:set
@time: 2018/1/8 11:42
"""


import sys

const_module = sys.modules["PYTHONIC_CONST"]

def set_const(name,value):
    const_module[name] = value

def clear():
    const_module.clear()

def set_v1():
    set_const("v1","value1")
    set_const("v2",99.99)
    set_const("v3",100)

