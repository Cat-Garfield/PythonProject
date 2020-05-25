# -*- coding:utf-8 -*-
import configparser

'''
配置文件读取类
'''


class ConfigHelper(object):
    _instance = None

    _config_path = r'config.ini'
    _config = configparser.ConfigParser(allow_no_value=True)
    _config.read(_config_path)

    def __init__(self):
        pass

    '''
    重写__new__方法实现单例
    '''

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super.__new__(cls)
        return cls._instance

    '''
    获取单个配置属性
    '''

    @staticmethod
    def _GetSection(section, item):
        try:
            ConfigHelper._config.get(section, item)
        except BaseException as e:
            print(e)

    '''
    获取Section下所有配置属性
    '''

    @staticmethod
    def _GetItems(section):
        try:
            items = ConfigHelper._config.items(section)
            return items
        except BaseException as e:
            print(e)

    '''
    获取Oracle数据库连接信息
    '''

    @staticmethod
    def GetOracleInfo():
        try:
            dbInfo = {}
            items = ConfigHelper._GetItems('OracleSession')
            for item in items:
                dbInfo.setdefault(item[0], item[1])
            return dbInfo
        except BaseException as e:
            print(e)
