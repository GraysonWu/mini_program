#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JeakoWu

import json
import random
import urllib.request as urllib2

import pymysql

from service import connect
from service.general_service import has_complete, user_exist_and_paired, get_user_id, get_couple_id

from config import app_config

def request_token_service(auth_code, inviter_id):

    url = "https://api.weixin.qq.com/sns/jscode2session?appid="+app_config['appid']+"&secret="\
          +app_config['secret']+"&js_code="+auth_code+"&grant_type=authorization_code"

    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    res_json = res.decode('utf-8')

    wechat_res = json.loads(s=res_json)

    result = dict()

    try:
        open_id = wechat_res["openid"]
    except:
        return False, "invalid code", "null"

    connection = connect()
    cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

    try:

        judgement = user_exist_and_paired(open_id)

        result["id"] = judgement[2]

        if not judgement[0]:

            query = "insert into user(open_id) values(%s)"

            try:
                cursor.execute(query, (open_id))

                connection.commit()

                result["id"] = get_user_id(open_id)[1]

            except:

                connection.rollback()

                connection.close()

                return False, "数据库连接失败", "null"

        user_id = result["id"]

        if inviter_id != -1:

            couple_id = get_couple_id(user_id)[1]

            if couple_id == inviter_id:

                return True, "情侣登录成功", result

            if judgement[1]:

                connection.close()

                return True, "有邀请人登录成功，但该用户已经配对无法接受邀请", result

            if user_exist_and_paired(inviter_id)[1]:

                connection.close()

                return True, "有邀请人登录成功，但邀请人已经配对无法接受邀请", result

            try:

                if inviter_id == user_id:

                    return True, "有邀请人登陆成功，但不能和自己配对", result

                else:
                    query = "update user set couple_id = %s where id = %s"

                    cursor.execute(query, (inviter_id, user_id))

                    cursor.execute(query, (user_id, inviter_id))

                    connection.commit()

                    connection.close()

                    return True, "有邀请人登录配对成功", result

            except:

                connection.rollback()

                connection.close()

                return True, "有邀请人登录成功，配对失败", result

        connection.close()

        return True, "无邀请人登录成功", result

    except:
        connection.close()

        return False, "数据库连接失败", "null"


def get_status_service(auth_token):

    connection = connect()

    try:

        cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

        query = "select * from user where id = %s"

        if cursor.execute(query, (auth_token)):

            connection.commit()

            user_state = cursor.fetchone()

            connection.close()

            return True, "获取用户信息成功", user_state

        else:

            connection.close()

            return False, "用户不存在", "null"


    except:
        connection.close()

        return False, "无法连接数据库", "null"


def get_report_service(auth_token):

    connection = connect()

    try:

        complete_condition = has_complete(auth_token)

        if complete_condition[0]:

            cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

            query = "select * from task where u_id = %s"

            if cursor.execute(query,(auth_token)):

                connection.commit()

                user_task = cursor.fetchone()

                if cursor.execute(query, (complete_condition[1])):

                    connection.commit()

                    couple_task = cursor.fetchone()

                    report = dict()
                    report["photo1"] = user_task["img_path"]
                    report["photo2"] = couple_task["img_path"]

                    if user_task["answer"] == couple_task["standard"] and user_task["standard"] == couple_task["answer"]:

                        conclusion_type = 1

                        report['score'] = 100

                    else:

                        conclusion_type = 0

                        report['score'] = random.randint(70, 99)

                    query = "select * from conclusion where conclusion_type = %s"

                    cursor.execute(query, (conclusion_type))

                    get_conclusion = random.sample(cursor.fetchall(), 1)

                    report["document"] = get_conclusion[0]['conclusion_text']

                    connection.close()

                    return True, "获取报告成功", report

                else:

                    connection.close()

                    return False, "获取伴侣信息失败", "null"
            else:

                connection.close()

                return False, "获取用户信息失败", "null"
        else:

             connection.close()

             return False, "需要等待双方完成", "null"

    except:

        connection.close()

        return False, "无法连接数据库", "null"


def get_egg_service(auth_token):

    connection = connect()

    try:

        cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

        query = "select * from user where id = %s"

        if cursor.execute(query, (get_couple_id(auth_token)[1])):

            connection.commit()

            egg_path = cursor.fetchone()

            query = "update user set egg_status = 2 where id = %s"

            try:

                cursor.execute(query, (auth_token))

                connection.commit()

            except:

                connection.rollback()

            connection.close()

            return True, "获取彩蛋成功", egg_path["egg_path"]

        else:

            connection.close()

            return False, "获取彩蛋失败", "null"

    except:

        connection.close()

        return False, "无法连接数据库", "null"