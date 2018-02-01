# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:test
@time: 2018/1/5 19:53
"""
import unittest
from key_words._global import project_name,replace_global_project_name,replace_project_name
from key_words._nonlocal import auto_inc

class TestKeyWords(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_replace(self):
        replace_project_name(20)
        #todo 这里的地址发生了改变
        from key_words._global import project_name
        self.assertNotEqual(project_name, 20)

    def test_replace_global(self):
        replace_global_project_name(20)
        # todo 这里的地址发生了改变
        from key_words._global import project_name
        self.assertEqual(project_name, 20)

    def test_auto_inc(self):
        inc = auto_inc(1)
        inc()
        inc()
        self.assertEqual(inc(),4)



