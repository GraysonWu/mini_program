#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JeakoWu

db_config_picker = dict()

db_config_development = dict()

db_config_development = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'sweetie',
    'charset': 'utf8',
    'save_path':'E:/sweetie/',
    'display_path':'E:/sweetie/'
}

db_config_production = dict()

db_config_production = {
    'host': '',
    'port': 3306,
    'user': '',
    'password': '',
    'db': 'sweetie',
    'charset': 'utf8',
    'save_path':'/var/lib/tomcat/webapps/ROOT/',
    'display_path':'http://xxxx.xxx:8080/'
}

db_config_picker['development'] = db_config_development
db_config_picker['production'] = db_config_production

app_config = dict()

app_config['appid'] = ""
app_config['secret'] = ""

