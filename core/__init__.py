# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/7/15 4:49 下午.
# Copyright (c) 2020 3KWan.
# Description :

from flask import Flask

from core.blueprint import index
from core.blueprint.auth import login
from core.blueprint.blog import blog
from core.blueprint.interface import interface
from core.extensions import db
from core.settings import configs


def create_app(config_name=None):
    """
        工厂函数

    :param config_name:
    :return:
    """

    # 默认测试环境
    _config = "development" if config_name is None else config_name

    app = Flask(__name__)
    app.config.from_object(configs[_config])

    # 注册蓝图
    register_blueprint(app)

    # 注册扩展
    register_extensions(app)

    return app


def register_blueprint(app):
    """
        注册蓝图

    :param app:
    :return:
    """

    app.register_blueprint(index.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(interface.bp)


def register_extensions(app):
    """ 注册扩展 """
    db.init_app(app)  # 数据库扩展
