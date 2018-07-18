# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:callback
@time: 2018/7/18 14:13
"""
import logging

class Framework:
    def __init__(self, callback):
        self.callback = callback

    def run(self):
        self.setup()
        self.callback()
        self.teardown()

    def setup(self):
        pass

    def teardown(self):
        pass


def your_function(level, message):
    print(level, message)



# 方法一 使用闭包
def configured_wrapper_logger(level, message):
    def _configured_logger():
        your_function(level, message)

    return _configured_logger



# 方法二，使用lambda
configured_lambda_logger = lambda: your_function(logging.ERROR, "ERROR logger")


# 方法三 使用class __call__
class ConfiguredLogger:
    def __init__(self, level, msg):
        self.level = level
        self.msg = msg

    def __call__(self):
        your_function(self.level, self.msg)
