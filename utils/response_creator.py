#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 20:15
# @Author  : JeakoWu
import json

from model.response_class import resp_class
from utils.type_change import class_2_dict


def response_creator(raw_result):
    response = resp_class(True, "", "null")

    response.isSuccess = raw_result[0]
    response.msg = raw_result[1]
    response.data = raw_result[2]

    resp_dict = class_2_dict(response)
    result = json.dumps(resp_dict, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False).encode('utf8')

    return result
