# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:signals
@time: 2018/7/17 23:57
"""
from signals.signals.signal import Signal

pre_init = Signal(providing_args=["instance", "args", "kwargs"])
post_init = Signal(providing_args=["instance"])

pre_save = Signal(providing_args=["instance", "raw"])
post_save = Signal(providing_args=["instance", "raw", "created"])

pre_delete = Signal(providing_args=["instance", "using"])
