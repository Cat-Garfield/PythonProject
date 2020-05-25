# —*- coding:utf-8 -*-

'''
定义一个数据库接口的抽象基类
'''
from abc import ABCMeta, abstractmethod


class IDbHelper(metaclass=ABCMeta):
    '''
    初始化数据库
    '''

    @abstractmethod
    def init(self):
        pass

    '''
    获取数据库链接
    '''

    @abstractmethod
    def get_connection(self):
        pass

    '''
    关闭数据库链接
    '''

    @abstractmethod
    def close_connection(self):
        pass

    '''
    执行数据库语句
    '''

    @abstractmethod
    def execute(self, sql, param=None):
        pass
