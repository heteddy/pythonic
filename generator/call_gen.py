# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:call_gen.py
@time: 2018/5/15 12:32
"""


def inner():
    i = 0
    while True:
        i = yield i
        print('inner',i)
        if i > 10:
            raise StopIteration


def outer():
    _in = 0
    _out = 1
    gen = inner()
    gen.send(None)

    while True:
        try:
            _in = gen.send(_out)
            _out = yield _in
            print('outer',_out)
        except StopIteration:   
            break

def simple_outer():
    yield from inner()


def main():
    o = simple_outer()
    o.send(None)
    i = 0
    while 1:
        try:
            i = o.send(i + 1)
            print(i)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
