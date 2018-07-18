# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:settings
@time: 2018/1/5 19:05
"""
import os
import sys

setting_path = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, setting_path)

TEST_CASES = [
    "key_words.test",
    "sys_module.test",
    "signals.test",
    "function.test"
]
