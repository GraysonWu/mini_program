#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JeakoWu

def class_2_dict(obj):
    tmp_dict = dict()
    tmp_dict.update(obj.__dict__)
    return tmp_dict

