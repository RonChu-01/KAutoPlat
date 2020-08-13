# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/8/7 4:04 下午.
# Copyright (c) 2020 3KWan.
# Description :

import random

from faker import Faker
from flask import Blueprint, render_template, jsonify, request

bp = Blueprint("interface", __name__, url_prefix="/interface")

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


@bp.route("/")
def index():

    # todo 需要做级联查询

    tasks = []

    fake = Faker("zh_CN")

    for i in range(50):
        task_info = dict()
        task_info.setdefault("task_id", i)
        task_info.setdefault("channel", random.choice([_ for _ in channel.keys()]))
        task_info.setdefault("buss_type", random.choice([_ for _ in ["国内", "独立", "海外"]]))
        task_info.setdefault("version", "v4")
        task_info.setdefault("task_type", random.choice([_ for _ in ["自建", "jenkins"]]))
        task_info.setdefault("task_status", random.choice([_ for _ in ["成功", "失败", "排队中", "执行中", "未执行"]]))
        task_info.setdefault("notice", random.choice([_ for _ in ["发送成功", "发送失败", "未发送"]]))
        task_info.setdefault("sponsor", random.choice([_ for _ in ["admin", "test", "dev"]]))
        task_info.setdefault("create_time", fake.date_time(tzinfo=None))
        task_info.setdefault("complete_time", fake.date_time(tzinfo=None))
        task_info.setdefault("test_report", "https://wwww.baidu.com")
        tasks.append(task_info)

    return render_template("interface/index.html", tasks=tasks)


# ======================== 数据接口 ========================

@bp.route("/api/v1/buss_type", methods=("GET", "POST"))
def api_v1_buss_type():
    """
        业务类型（数据接口）

    :return:
    """

    # todo 这里为模拟数据，待建表
    # 处理策略，选择业务类型的时候就先去查询下级
    data = {
        "0": "国内",
        "1": "独立",
        "2": "海外"
    }

    return jsonify({
        "code": 0,
        "msg": "",
        "data": data
    })


@bp.route("/api/v1/channel", methods=("GET", "POST"))
def api_v1_channel():
    """
        渠道

    :return:
    """

    data = {
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

    return jsonify({
        "code": 0,
        "msg": "",
        "data": data
    })


@bp.route("/api/v1/version", methods=("GET", "POST"))
def api_v1_api_version():
    """
        接口版本

    :return:
    """

    data = {
        "0": "全部",
        "1": "V3",
        "2": "V4",
        "3": "V5"
    }

    return jsonify({
        "code": 0,
        "msg": "",
        "data": data
    })


@bp.route("/api/v1/task_type", methods=("GET", "POST"))
def api_v1_task_type():
    """
        任务类型

    :return:
    """
    data = {
        "0": "全部",
        "1": "自建",
        "2": "Jenkins",
    }

    return jsonify({
        "code": 0,
        "msg": "",
        "data": data
    })


@bp.route("/api/v1/task_status", methods=("GET", "POST"))
def api_v1_task_status():
    """
        任务状态

    :return:
    """
    data = {
        "0": "全部",
        "1": "未执行",
        "2": "排队中",
        "3": "执行中",
        "4": "测试通过",
        "5": "测试失败",
    }

    return jsonify({
        "code": 0,
        "msg": "",
        "data": data
    })


@bp.route("/api/v1/search_by_condition", methods=("GET", "POST"))
def api_v1_search_by_condition():
    """
        按条件搜索

    :return:
    """

    params = request.get_json()

    tasks = []

    fake = Faker("zh_CN")

    for i in range(20):
        task_info = dict()
        task_info.setdefault("task_id", i)
        task_info.setdefault("channel", random.choice([_ for _ in channel.keys()]))
        task_info.setdefault("buss_type", random.choice([_ for _ in ["国内", "独立", "海外"]]))
        task_info.setdefault("version", "v4")
        task_info.setdefault("task_type", random.choice([_ for _ in ["自建", "jenkins"]]))
        task_info.setdefault("task_status", random.choice([_ for _ in ["成功", "失败", "排队中", "执行中", "未执行"]]))
        task_info.setdefault("notice", random.choice([_ for _ in ["发送成功", "发送失败", "未发送"]]))
        task_info.setdefault("sponsor", random.choice([_ for _ in ["admin", "test", "dev"]]))
        task_info.setdefault("create_time", fake.date_time(tzinfo=None))
        task_info.setdefault("complete_time", fake.date_time(tzinfo=None))
        task_info.setdefault("test_report", "https://wwww.baidu.com")
        tasks.append(task_info)

    return jsonify({
        "code": 0,
        "msg": "ok",
        "data": tasks
    })


# if __name__ == '__main__':
#     data = [1, 2, 2, 3, 5, 6]
#     print(random.choice([c for c in channel.keys()]))

