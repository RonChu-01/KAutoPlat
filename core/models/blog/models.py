# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/7/17 2:37 下午.
# Copyright (c) 2020 3KWan.
# Description :

from datetime import datetime

from core.models.base import BaseTable
from core.extensions import db


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
