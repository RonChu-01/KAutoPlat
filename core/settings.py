# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/7/15 5:10 下午.
# Copyright (c) 2020 3KWan.
# Description :

import os


class BaseConfig:
    """ 基础配置 """
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_COMMIT_TEARDOWN = True


class ProductionConfig(BaseConfig):
    """ 生产环境 """


class TestingConfig(BaseConfig):
    """ 测试环境 """


class DevelopmentConfig(BaseConfig):
    """ 开发环境 """
    SQLALCHEMY_DATABASE_URI = "mysql://root:chuy5945@localhost/autoplat?charset=utf8"  # mysql连接（本地mysql）


# 配置映射
configs = {
    "production": ProductionConfig,
    "testing": TestingConfig,
    "development": DevelopmentConfig
}
