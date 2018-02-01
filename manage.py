# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:manage
@time: 2018/1/5 19:05
"""
import importlib
# import inspect
import os
import sys
import unittest

import settings


def run_tests():
    suites = list()
    for t in settings.TEST_CASES:
        module = importlib.import_module(t)

        # for c in dir(module):
        #     cls = getattr(module, c)
        #     if inspect.isclass(cls):
        #         suite.addTest(cls())
        suite = unittest.TestLoader().loadTestsFromModule(module)

        suites.append(suite)


    test_suite = unittest.TestSuite(suites)
    '''
    verbosity
    0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共100个 失败20 成功80
    1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.”  每个失败的用例前面有个 “F”
    2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
    '''
    unittest.TextTestRunner(verbosity=2).run(test_suite)


if __name__ == "__main__":
    # os.environ.setdefault("PYTHONIC", "settings")

    run_tests()
