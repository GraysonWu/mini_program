#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JeakoWu


from flask import Blueprint, request

from service.user_service import request_token_service, get_status_service, get_report_service, get_egg_service
from utils.hd_base import require
from utils.response_creator import response_creator

user = Blueprint('user', __name__)


@user.route('/request_token', methods=['POST'])
@require('code','inviter_id')
def request_token():

    if request.method == 'POST':
        auth_token = request.json.get('code')
        get_inviter_id = int(request.json.get('inviter_id'))

    raw_result = request_token_service(auth_token, get_inviter_id)

    result = response_creator(raw_result)
    return result


@user.route('/get_status', methods=['POST'])
@require('token')
def get_status():

    if request.method == 'POST':
        auth_token = request.json.get('token')

    get_user_state = get_status_service(auth_token)

    if get_user_state[0]:

        get_couple_state = get_status_service(get_user_state[2]["couple_id"])

        resp_data = {"user": get_user_state[2], "couple": get_couple_state[2]}

        raw_result = [get_user_state[0], get_user_state[1], resp_data]
        result = response_creator(raw_result)

    else:
        result = response_creator(get_user_state)

    return result

@user.route('/get_report', methods=['POST'])
@require('token')
def get_report():

    if request.method == 'POST':
        auth_token = request.json.get('token')

    raw_result = get_report_service(auth_token)

    result = response_creator(raw_result)
    return result


@user.route('/get_egg', methods=['POST'])
@require('token')
def get_egg():

    if request.method == 'POST':
        auth_token = request.json.get('token')

    raw_result = get_egg_service(auth_token)
    result = response_creator(raw_result)

    return result

