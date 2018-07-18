# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:example
@time: 2018/7/18 11:09
"""
from signals.models.model import Model
from signals.models.signals import pre_init, post_init, post_save
from signals.signals.signal import receiver


class TestTable(Model):
    """
    这里模拟一个测试table
    """

    class Meta:
        app_label = "signals.test"
        verbose_name = "测试"


@receiver([pre_init, post_init], sender=TestTable)
def process_table_init(sender, instance, **kwargs):
    print("process_table_init")


@receiver(post_save, sender=TestTable)
def process_table_save(sender, instance, created, **kwargs):
    print("process_table_save", id(instance), created)
