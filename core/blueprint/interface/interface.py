# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/8/7 4:04 下午.
# Copyright (c) 2020 3KWan.
# Description :

import random

from faker import Faker
from flask import Blueprint, render_template, jsonify, request
from sqlalchemy import or_

from core.models.interface.models import TaskInfo

bp = Blueprint("interface", __name__, url_prefix="/interface")


@bp.route("/<int:page>", methods=("GET", "POST"))
def index(page):
    """

    :param page:
    :return:
    """

    if page is None:
        page = 1

    tasks = TaskInfo.query.order_by(TaskInfo.create_time.desc()).paginate(page=page, per_page=10)

    return render_template("interface/index.html", tasks=tasks)


@bp.route("/new_task", methods=("GET", "POST"))
def new_task():
    """

    :return:
    """
    return render_template("interface/new_task.html")


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

    results = []

    params = request.get_json()

    # 按条件筛选测试任务
    rows = TaskInfo.query.filter(
        or_(
            TaskInfo.id == params.get("id"),
            TaskInfo.buss_type == params.get("buss_type"),
            TaskInfo.channel_name == params.get("channel_name"),
            TaskInfo.sdk_version == params.get("sdk_version"),
            TaskInfo.task_type == params.get("task_type"),
            TaskInfo.task_status == params.get("task_status")
        )
    ).all()

    # 如果按条件查询结果存在，返回查询结果，否则返回全部数据
    if rows:
        for row in rows:
            result = row.multi_to_dict()
            results.append(result)
    else:
        rows = TaskInfo.query.all()
        for row in rows:
            result = row.multi_to_dict()
            results.append(result)

    return jsonify({
        "code": 0,
        "msg": "ok",
        "data": results
    })


@bp.route("/api/v1/add_task", methods=("GET", "POST"))
def api_v1_add_task():
    """
        新增测试任务（入库）

    :return:
    """

    params = request.get_json()

    return jsonify({
        "code": 0,
        "msg": "ok",
        "data": ""
    })


# if __name__ == '__main__':
#     data = [1, 2, 2, 3, 5, 6]
#     print(random.choice([c for c in channel.keys()]))

