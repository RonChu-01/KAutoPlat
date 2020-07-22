# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/7/20 5:08 下午.
# Copyright (c) 2020 3KWan.
# Description :

""" 生成虚拟数据 """

import random
from random import choice

from faker import Faker

from core import create_app
from core.business.db.blog.db import insert_into_blog

tags = ["随笔", "总结/心得", "书/影/音评", "计划", "运动/健身", "理财", "美食"]


def generate_blog_virtual_data(app=create_app(), num=50):
    """ 生成虚拟数据（blog文章） """
    print("==== start generate blog virtual data.")
    for _ in range(num):
        fake = Faker("zh_CN")
        title = fake.sentence(nb_words=6, variable_nb_words=True)  # 随机标题
        author = fake.name()  # 随机作者
        content = fake.text(max_nb_chars=random.randint(50, 500))  # 正文
        tag = choice(tags)  # 标签
        create_time = fake.date_time(tzinfo=None)  # 随机日期时间
        last_update_time = fake.date_time(tzinfo=None)  # 随机日期时间

        _data = {
            "title": title,
            "author": author,
            "content": content,
            "tag": tag,
            "create_time": create_time,
            "last_update_time": last_update_time
        }

        with app.app_context():
            insert_into_blog(**_data)

    print("==== finish generate blog virtual data")


if __name__ == '__main__':
    generate_blog_virtual_data()
