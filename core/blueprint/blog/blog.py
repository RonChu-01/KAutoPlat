# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/7/17 10:40 上午.
# Copyright (c) 2020 3KWan.
# Description :

from flask import Blueprint, render_template

from core.models.blog.models import Blog

bp = Blueprint("blog", __name__, url_prefix="/blog")


@bp.route("/<int:page>", methods=("GET", "POST"))
def index(page=None):

    if page is None:
        page = 1

    page_data = Blog.query.order_by(Blog.last_update_time.desc()).paginate(page=page, per_page=10)

    return render_template("blog/index.html", data=page_data)
