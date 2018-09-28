#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/8 19:17
# @Author  : JeakoWu
import pymysql

from service import connect

def get_user_id(auth_token):

    connection = connect()
    try:

        cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

        query = "select * from user where open_id = %s"

        if cursor.execute(query, auth_token):
            user_id = cursor.fetchone()
            connection.close()

            return True, user_id["id"]
        else:
            connection.close()

            return False, "null"
    except:
        connection.close()

        return False, "无法连接数据库"


def get_couple_id(auth_token):
    connection = connect()
    try:

        cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

        query = "select * from user where id = %s"

        if cursor.execute(query, auth_token):

            user_id = cursor.fetchone()

            connection.close()

            return True, user_id["couple_id"]

        else:
            connection.close()

            return False, "null"
    except:
        connection.close()

        return False, "无法连接数据库"


def has_complete(auth_token):
    connection = connect()
    try:

        cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

        query = "select * from user where id = %s"

        if cursor.execute(query, auth_token):

            connection.commit()

            current_user = cursor.fetchone()

            if current_user["task_proc"] == 2:

                if cursor.execute(query, current_user["couple_id"]):

                    connection.commit()

                    if cursor.fetchone()["task_proc"] == 2:

                        connection.close()

                        return True, current_user["couple_id"]

        connection.close()

        return False, -1

    except:
        connection.close()

        return False, -1


def user_exist_and_paired(auth_token):

    connection = connect()

    try:

        cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

        query = "select * from user where open_id = %s"

        if cursor.execute(query, auth_token):

            connection.commit()

            user_info = cursor.fetchone()

            if user_info["couple_id"] == -1:
                connection.close()

                return True, False, user_info["id"]    # 是否存在 是否配对 id是几
            else:
                connection.close()

                return True, True, user_info["id"]
        else:
            connection.close()

            return False, False, -1

    except:
        connection.close()

        return False, False, -1
