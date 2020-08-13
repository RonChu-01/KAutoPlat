# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/7/20 5:08 下午.
# Copyright (c) 2020 3KWan.
# Description :

""" 生成虚拟数据 """

import random
from random import choice

from faker import Faker

from core import create_app
from core.business.db.blog.db import insert_into_blog, insert_into_task_info

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


channel = {
    "3k": "3k",
    "360": "360",
    "mi": "小米",
    "91": "91",
    "wandou": "豌豆荚",
    "dangle": "当乐",
    "oppo": "oppo",
    "duoku": "百度",
    "uc": "uc",
    "huawei": "华为",
    "vivo": "步步高",
    "4399": "4399"
}


def generate_task_info_virtual_data(app=create_app(), num=50):
    """
        生成虚拟数据（任务信息）

    :param app:
    :param num:
    :return:
    """

    fake = Faker("zh_CN")

    for i in range(num):
        task_info = dict()
        task_info.setdefault("channel_name", random.choice([_ for _ in channel.keys()]))
        task_info.setdefault("buss_type", random.choice([_ for _ in ["国内", "独立", "海外"]]))
        task_info.setdefault("sdk_version", random.choice([_ for _ in ["V3", "V4", "V5"]]))
        task_info.setdefault("task_type", random.choice([_ for _ in ["自建", "jenkins"]]))
        task_info.setdefault("task_status", random.choice([_ for _ in ["成功", "失败", "排队中", "执行中", "未执行"]]))
        task_info.setdefault("wechat_notice_status", random.choice([_ for _ in ["发送成功", "发送失败", "未发送"]]))
        task_info.setdefault("sponsor", random.choice([_ for _ in ["admin", "test", "dev"]]))
        task_info.setdefault("create_time", fake.date_time(tzinfo=None))
        task_info.setdefault("complete_time", fake.date_time(tzinfo=None))
        task_info.setdefault("test_report", "https://wwww.baidu.com")

        with app.app_context():
            insert_into_task_info(**task_info)


if __name__ == '__main__':
    # generate_blog_virtual_data()
    generate_task_info_virtual_data()
