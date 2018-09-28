#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/8 14:05
# @Author  : JeakoWu

class resp_class:
    def __init__(self, isSuccess, msg, data):
        self.isSuccess = isSuccess
        self.msg = msg
        self.data = data