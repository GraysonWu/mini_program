#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JeakoWu

from flask import Blueprint
from flask import flash, request, redirect

from service.task_service import upload_audio_service, submit_task1_service, submit_task2_service, \
    task1_question_service
from utils.hd_base import require
from utils.response_creator import response_creator

task = Blueprint('task', __name__)


@task.route('/upload_audio', methods=['POST'])
def upload_audio():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        auth_token = request.form['token']

    upload_audio_result = upload_audio_service(auth_token, file)
    result = response_creator(upload_audio_result)

    return result


@task.route('/task1_question', methods=['GET'])
def task1_question():

    get_question = task1_question_service()
    result = response_creator(get_question)

    return result


@task.route('/submit_task1', methods=['POST'])
@require("token", "answer", "standard")
def submit_task1():
    if request.method == 'POST':
        get_answer = request.json.get('answer')
        get_standard = request.json.get('standard')
        auth_token = request.json.get('token')

    task1_submit_result = submit_task1_service(auth_token, get_answer, get_standard)
    result = response_creator(task1_submit_result)

    return result


@task.route('/submit_task2', methods=['POST'])
def submit_task2():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        auth_token = request.form['token']

    task2_submit_result = submit_task2_service(auth_token, file)
    result = response_creator(task2_submit_result)

    return result