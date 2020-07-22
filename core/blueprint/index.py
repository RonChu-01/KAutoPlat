# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/7/15 5:23 下午.
# Copyright (c) 2020 3KWan.
# Description :

from flask import Blueprint, render_template, request, session, redirect, url_for

import flask_login


bp = Blueprint("index", __name__, url_prefix="/index")


@bp.route("/", methods=("GET", "POST"))
def index():

    if "username" in session:
        return render_template("index.html")
    else:
        return redirect(url_for("login.login"))

