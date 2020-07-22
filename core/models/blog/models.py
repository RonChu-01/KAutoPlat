# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/7/17 2:37 下午.
# Copyright (c) 2020 3KWan.
# Description :

from datetime import datetime

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


class Blog(BaseTable):
    """ 博客表 """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))  # 标题
    content = db.Column(db.Text)  # 正文
    tag = db.Column(db.String(64))  # 分类/标签
    author = db.Column(db.String(64))  # 作者
    create_time = db.Column(db.DateTime, default=datetime.now, index=True)  # 创建时间
    last_update_time = db.Column(db.DateTime, default=datetime.now, index=True)  # 最后编辑时间


# if __name__ == '__main__':
#     from core import create_app
#     app = create_app()
#     with app.app_context():
#         # db.drop_all()
#         db.create_all()
