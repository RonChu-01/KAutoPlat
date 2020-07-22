# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/7/21 11:34 上午.
# Copyright (c) 2020 3KWan.
# Description :


from flask import Blueprint, redirect, url_for, session


bp = Blueprint("logout", __name__, url_prefix="/logout")


@bp.route("/")
def logout():
    session.pop("username", "")
    return redirect(url_for("login.login"))


