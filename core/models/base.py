# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/8/13 4:02 下午.
# Copyright (c) 2020 3KWan.
# Description :

from core.extensions import db


class BaseTable(db.Model):
    """ 表格基类 """
    # Flask-SQLAlchemy创建table时,如何声明基类（这个类不会创建表,可以被继承）
    # 方法就是把__abstract__这个属性设置为True,这个类为基类，不会被创建为表！

    __abstract__ = True
    # extend_existing = True

    id = db.Column(db.Integer, primary_key=True)

    def single_to_dict(self):
        """ 查询数据转换 """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def multi_to_dict(self):
        """ 查询数据转换 """
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result

