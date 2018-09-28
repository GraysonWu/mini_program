#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JeakoWu

import pymysql

from config import db_config_picker

# config = db_config_picker['development']
config = db_config_picker['production']


def connect():

    connection = pymysql.connect(host=config['host'], user=config['user'], port=config['port'],
                              passwd=config['password'],
                             db=config['db'], charset=config['charset'])

    return connection
