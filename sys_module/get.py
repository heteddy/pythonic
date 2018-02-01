# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:get
@time: 2018/1/8 11:42
"""
import sys

const_module = sys.modules["PYTHONIC_CONST"]


def get_value(name):
    return const_module[name]
