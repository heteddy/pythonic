# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:const
@time: 2018/1/8 11:05
"""
import sys

class ConstChangeFailureException(Exception):
    def __init__(self):
        super(ConstChangeFailureException, self).__init__()
    def __str__(self):
        return "ConstChangeFailureException"


class ProjectConst(dict):
    def __init__(self):
        super(ProjectConst, self).__init__()


    def __setitem__(self, key, value):
        if key in self:
            raise ConstChangeFailureException()
        else:
            return super(ProjectConst, self).__setitem__(key,value)


sys.modules["PYTHONIC_CONST"] = ProjectConst()

