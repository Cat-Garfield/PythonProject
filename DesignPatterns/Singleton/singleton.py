# -*- coding:utf-8 -*-
'''
单例模式
'''


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            Singleton._instance = object.__new__(cls)
        return Singleton._instance


class A(Singleton):
    def __init__(self, param):
        self.txt = param


class B(Singleton):
    def __init__(self, param):
        self.txt = param


a = A('aaaa')
print(a.txt)
b = B('bbbb')
print(b.txt)
b.txt = '2222'
print(a.txt)
print(b.txt)
