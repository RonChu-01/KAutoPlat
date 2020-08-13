# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/7/20 5:45 下午.
# Copyright (c) 2020 3KWan.
# Description :

from core.extensions import db
from core.models.blog.models import Blog
from core.models.interface.models import TaskInfo


def insert_into_blog(**data):
    """ 博客入库 """

    blog = Blog(**data)
    db.session.add(blog)
    db.session.commit()


def insert_into_task_info(**data):
    """ 任务信息入库 """
    blog = TaskInfo(**data)
    db.session.add(blog)
    db.session.commit()



