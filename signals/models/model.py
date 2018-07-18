# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:model
@time: 2018/7/17 23:20
"""
from random import choice

from signals.models.signals import *


class ModelBase(type):
    def __new__(cls, name, bases, attrs):
        '''
        获取 meta class app_label,获取表名称
        :param name:
        :param bases:
        :param attrs:
        :return:
        '''
        super_new = super(ModelBase, cls).__new__
        module = attrs.pop('__module__')

        attrs.update({'__module__': module})
        new_class = super_new(cls, name, bases, attrs)
        attr_meta = attrs.pop('Meta', None)

        if not attr_meta:
            meta = getattr(new_class, 'Meta', None)
        else:
            meta = attr_meta
        setattr(new_class, '_meta', meta)
        return new_class


# class Model(object, metaclass=ModelBase):
class Model(object, metaclass=ModelBase):
    def __init__(self):
        pre_init.send(sender=self.__class__, instance=self)
        # todo add init code

        post_init.send(sender=self.__class__, instance=self)

    def save(self):
        pre_save.send(sender=self.__class__, raw=self, instance=self)

        post_save.send(sender=self.__class__, instance=self, created=choice([True, False]))
