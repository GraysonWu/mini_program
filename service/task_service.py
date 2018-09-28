#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JeakoWu
import pymysql

from service import config
from service import connect

ALLOWED_EXTENSIONS_PHOTO = set(['png', 'jpg', 'jpeg'])

UPLOAD_FOLDER_PHOTO = config['save_path'] + "photo/"#文件夹必须存在

ALLOWED_EXTENSIONS_AUDIO = set(['mp3', 'wma', 'wav'])

UPLOAD_FOLDER_AUDIO = config['save_path'] + "audio/"#文件夹必须存在


def allowed_file_audio(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS_AUDIO


def allowed_file_photo(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS_PHOTO


def upload_audio_service(auth_token, file):

    connection = connect()

    try:

        if file and allowed_file_audio(file.filename):

            filename = file.filename

        else:

            return False, "彩蛋上传失败,只能上传mp3、wma、wav格式", "null"

        new_filename = auth_token + "." + str(filename).split(".")[1]

        audio_path = UPLOAD_FOLDER_AUDIO + new_filename

        file.save(str(audio_path))

        cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

        egg_path = config['display_path'] + "audio/" + new_filename

        query = "update user set egg_status = 1, egg_path = %s where id = %s"

        try:

            cursor.execute(query, (egg_path, auth_token))

            connection.commit()

            connection.close()

            return True, "彩蛋上传成功", "null"

        except:

            connection.rollback()

            connection.close()

            return False, "彩蛋上传失败", "null"

    except:

        connection.close()

        return False, "无法连接数据库", "null"


def task1_question_service():

    connection = connect()

    try:

        cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

        query = "select * from question"

        if cursor.execute(query):

            connection.commit()

            questions = cursor.fetchall()

            connection.close()

            return True, "获取问题成功", questions

        else:

            connection.close()

            return False, "获取问题失败", "null"

    except:

        connection.close()

        return False, "无法连接数据库", "null"


def submit_task1_service(auth_token, get_answer, get_standard):

    connection = connect()

    try:

        cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

        insert_query = "insert into task(u_id,answer,standard) values(%s,%s,%s)"

        update_query = "update user set task_proc = 1 where id = %s"

        try:

            cursor.execute(insert_query, (auth_token, get_answer, get_standard))

            cursor.execute(update_query, auth_token)

            connection.commit()

            connection.close()

            return True, "Success", "null"

        except:

            connection.rollback()

            connection.close()

            return False, "用户已经提交过任务", "null"

    except:

        connection.close()

        return False, "无法连接数据库", "null"


def submit_task2_service(auth_token,file):

    connection = connect()

    try:

        if file and allowed_file_photo(file.filename):

            filename = file.filename

        else:

            return False, "图片上传失败,只能上传png、jpg、jpeg格式", "null"

        new_filename = auth_token + "." + str(filename).split(".")[1]

        img_path = UPLOAD_FOLDER_PHOTO + new_filename

        file.save(str(img_path))

        cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

        img_path = config['display_path'] + "photo/" + new_filename

        task_query = "update task set img_path = %s where u_id = %s"

        user_query = "update user set task_proc = 2 where id = %s"

        try:

            cursor.execute(task_query, (img_path, auth_token))

            cursor.execute(user_query, auth_token)

            connection.commit()

            connection.close()

            return True, "图片上传成功", "null"

        except:

            connection.rollback()

            connection.close()

            return False, "图片上传失败", "null"

    except :

        connection.close()

        return False, "无法连接数据库", "null"
