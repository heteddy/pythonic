# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:signal
@time: 2018/7/17 23:21
"""


def _make_id(target):
    return id(target)


class Signal(object):
    """
    base class of signal
    """

    def __init__(self, providing_args=None):
        self.receivers = []
        if providing_args is None:
            providing_args = []
        self.providing_args = set(providing_args)

    def connect(self, receiver, sender=None, dispatch_uid=None):
        '''

        :param receiver: 根据receiver函数的实现 (connect(function, sender) )
        :param sender:
        :param dispatch_uid:
        :return:
        '''
        if dispatch_uid:
            lookup_key = (dispatch_uid, _make_id(sender))
        else:
            lookup_key = (_make_id(receiver), _make_id(sender))

        for r_key, _ in self.receivers:
            # 不能重复注册
            if r_key == lookup_key:
                break
        else:
            self.receivers.append((lookup_key, receiver))

    def disconnect(self, receiver=None, sender=None, dispatch_uid=None):

        if dispatch_uid:
            lookup_key = (dispatch_uid, _make_id(sender))
        else:
            lookup_key = (_make_id(receiver), _make_id(sender))

        for index in range(len(self.receivers)):
            (r_key, _) = self.receivers[index]
            if r_key == lookup_key:
                del self.receivers[index]
                break

    def send(self, sender, **named):

        responses = []
        if not self.receivers:
            return responses

        for receiver in self._live_receivers(_make_id(sender)):
            # 这里的receiver实际上是我们自定义的函数
            response = receiver(signal=self, sender=sender, **named)
            responses.append((receiver, response))
        return responses

    def _live_receivers(self, sender_key):
        none_sender_key = _make_id(None)
        receivers = list()

        for (receiver_key, r_sender_key), receiver in self.receivers:

            if r_sender_key == none_sender_key or r_sender_key == sender_key:
                receivers.append(receiver)
        return receivers


def receiver(signal, **kwargs):
    def _decorator(func):
        if isinstance(signal, (list, tuple)):
            for s in signal:
                s.connect(func, **kwargs)
        else:
            signal.connect(func, **kwargs)
        return func

    return _decorator
