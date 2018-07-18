# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:test
@time: 2018/7/17 23:22
"""

import unittest
from signals.example import *


class TestSignal(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        t = TestTable()
        self.assertEqual(t._meta.app_label, "signals.test")
        self.assertEqual(t._meta.verbose_name, "测试")

    def test_save(self):
        t = TestTable()
        t.save()
