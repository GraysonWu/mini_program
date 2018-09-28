#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JeakoWu

from flask import Flask

from app.user import user
from app.task import task


app = Flask(__name__)

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(task, url_prefix='/task')