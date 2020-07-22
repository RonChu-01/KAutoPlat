# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/7/20 5:45 下午.
# Copyright (c) 2020 3KWan.
# Description :
from core.extensions import db
from core.models.blog.models import Blog


def insert_into_blog(**data):
    """ 博客入库 """

    blog = Blog(**data)
    db.session.add(blog)
    db.session.commit()


def query_all_blog():
    """ 获取全部文章 """

    try:
        rows = db.session.query(Blog).filter().all()
    except Exception as e:
        print(str(e))
        return None
    else:

        results = []

        if rows:
            for row in rows:
                result = row.multi_to_dict()
                results.append(result)

            return results

        else:
            return None
