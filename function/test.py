# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:test
@time: 2018/7/18 14:24
"""
import functools
import unittest

from function.callback import *


class TestCallBackWithArgs(unittest.TestCase):
    def test_wrapper_logger(self):
        f = Framework(configured_wrapper_logger(logging.INFO, "INFO logger"))
        f.run()

    def test_lambda_logger(self):
        f = Framework(configured_lambda_logger)
        f.run()

    def test_class_logger(self):
        f = Framework(ConfiguredLogger(logging.WARNING, 'WARNING logger'))
        f.run()

    def test_partial_logger(self):
        f = Framework(functools.partial(your_function, logging.DEBUG, 'DEBUG logger'))
        f.run()
