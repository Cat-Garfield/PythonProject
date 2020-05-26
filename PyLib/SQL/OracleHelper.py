# -*- coding:utf-8 -*-
'''
数据库：Oracle

'''
import cx_Oracle

from PyLib.SQL.IDbHelper import IDbHelper


class SQLHelper(IDbHelper):
    # 定义数据库链接
    __connection = None

    def __init__(self, configInfo):
        self.init(configInfo)

    '''
    初始化数据库链接
    '''
    def init(self, config):
        try:
            self.__connection = cx_Oracle.connect(config['DB_USER'], config['DB_PASS'], config['DB_TNS'])
        except BaseException as e:
            print(e)

    '''
    获取数据库链接
    '''
    def get_connection(self):
        if self.__connection:
            return self.__connection
        else:
            self.init()
            return self.__connection

    '''
    关闭数据库链接
    '''
    def close_connection(self):
        if self.__connection:
            self.__connection.close()

    '''
    执行SQL语句
    '''
    def execute(self, sql, param=None):
        try:
            data = None
            cur = self._NewCursor()
            if cur:
                data = cur.execute(sql, param)
                self._CloseCursor()
            return data
        except BaseException as e:
            print(e)

    '''
    创建数据库游标，又来获取数据
    '''
    def _NewCursor(self):
        cur = self.__connection.cursor()
        if cur:
            return cur
        else:
            return None

    '''
    关闭数据库游标
    '''
    def _CloseCursor(self, cur):
        if cur:
            cur.close()
