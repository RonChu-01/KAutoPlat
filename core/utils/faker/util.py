# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/7/20 5:02 下午.
# Copyright (c) 2020 3KWan.
# Description :

from faker import Faker


class GenerateVirtualData:
    """ 生成虚拟数据 """

    def __init__(self):
        self.fake = Faker("zh_CN")

