# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:nonlocal
@time: 2018/1/5 18:32
"""


# from functools import wraps,partial
#
# def attach_wrapper(obj, func=None):
#     if func is None:
#         return partial(attach_wrapper,obj)
#
#     setattr(obj,func.__name__,func)
#     return func


def auto_inc(start):
    counter = start

    def _inc():
        # todo 去掉 nonlocal报错
        nonlocal counter
        counter += 1
        return counter

    return _inc


if __name__ == '__main__':
    a = auto_inc(1)
    a()
    a()
    a()
