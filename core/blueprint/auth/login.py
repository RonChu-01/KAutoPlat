# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/7/21 11:34 上午.
# Copyright (c) 2020 3KWan.
# Description :

from flask import Blueprint, render_template, request, jsonify, make_response, session

bp = Blueprint("login", __name__, url_prefix="/login")


@bp.route("/", methods=("GET", "POST"))
def login():

    error = None

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if not username or not username == "admin":
            error = "用户名为空或不存在该用户，请检查"

        if not password or not password == "1":
            error = "密码为空或错误"

        if error is None:
            # 保存登录信息
            session["username"] = username
            session["password"] = password
            resp = make_response(render_template('index.html'))
            resp.set_cookie('username', username)

            return jsonify({
                "status": 0,
                "msg": "登录成功",
                "data": ""
            })

        else:
            return jsonify({
                "status": -1,
                "msg": error,
                "data": ""
            })

    return render_template("auth/login.html")

