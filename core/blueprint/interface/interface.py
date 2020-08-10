# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/8/7 4:04 下午.
# Copyright (c) 2020 3KWan.
# Description :

from flask import Blueprint, render_template, jsonify

bp = Blueprint("interface", __name__, url_prefix="/interface")


@bp.route("/")
def index():
    return render_template("interface/index.html")


# ======================== 数据接口 ========================

@bp.route("/api/v1/buss_type", methods=("GET", "POST"))
def api_v1_buss_type():
    """
        业务类型（数据接口）

    :return:
    """

    # todo 这里为模拟数据，待建表
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


@bp.route("/api/v1/channel")
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


@bp.route("/api/v1/api/version")
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


@bp.route("/api/v1/task_type")
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


@bp.route("/api/v1/task_status")
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

