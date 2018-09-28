#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JeakoWu

from flask import request, jsonify
import functools


def require(*required_args) -> object:
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            for arg in required_args:
                if arg not in request.json:
                    return jsonify(code=400, msg='参数不正确')
            return func(*args, **kw)
        return wrapper
    return decorator
