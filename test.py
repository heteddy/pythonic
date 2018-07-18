# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:test.py
@time: 2018/3/14 20:29
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self, values=None):
        self.root = None
        if values:
            for v in values[1:]:
                # self.insert(v)
                pass

    def insert(self, root, left, right):
        if root:
            root.left = left
            root.right = right

    def invert_tree(self, node):
        if node == None:
            return None
        left, right = node.right, node.left
        self.invert_tree(left)
        self.invert_tree(right)
