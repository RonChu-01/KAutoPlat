# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/8/13 4:02 下午.
# Copyright (c) 2020 3KWan.
# Description :


from core.models.base import BaseTable


class TaskInfo(BaseTable):
    """ 任务信息表 """

    id = db.Column(db.Integer, primary_key=True)
    channel_name = db.Column(db.String(8))  # 渠道
    buss_type = db.Column(db.String(8))  # 业务类型 ["国内", "独立", "海外"]
    sdk_version = db.Column(db.String(8))  # sdk版本
    task_type = db.Column(db.String(8))  # 任务类型 ["自建", "jenkins"]
    task_status = db.Column(db.String(8))  # 任务状态 ["成功", "失败", "排队中", "执行中", "未执行"]
    wechat_notice_status = db.Column(db.String(8))  # 微信通知状态 ["发送成功", "发送失败", "未发送"]
    sponsor = db.Column(db.String(8))  # 发起人
    create_time = db.Column(db.DateTime, default=datetime.now, index=True)  # 任务开始时间
    complete_time = db.Column(db.DateTime, default=datetime.now, index=True)  # 任务完成时间
    test_report = db.Column(db.String(32))  # 测试报告

