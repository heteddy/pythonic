# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:test
@time: 2018/1/8 11:45
"""
import unittest

from sys_module.const import ConstChangeFailureException
from sys_module.get import get_value
from sys_module.set import set_const, set_v1,clear


class TestSysModule(unittest.TestCase):
    def setUp(self):
        set_v1()

    def tearDown(self):
        clear()

    def test_set_duplicate(self):
        self.assertRaises(ConstChangeFailureException, set_const, "v1", "value2")

    def test_get_value(self):
        v1 = get_value("v1")
        v2 = get_value("v2")
        v3 = get_value("v3")

        self.assertEqual(v1, "value1")
        self.assertEqual(v2, 99.99)
        self.assertEqual(v3, 100)
