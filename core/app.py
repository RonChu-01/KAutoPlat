# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/7/15 4:52 下午.
# Copyright (c) 2020 3KWan.
# Description :

from core import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(
        port=10010
    )
