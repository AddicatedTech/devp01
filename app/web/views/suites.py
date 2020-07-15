#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 21:35
# @Author  : Addicated
# @Site    : 
# @File    : suites.py
# @Software: PyCharm

from app.web import web


@web.route('/suites')
def suites():
    return 'suites'


@web.route('/get_suite/<int:s_id>')
def get_suite(s_id=None):
    return f'get project {s_id}'


@web.route('/edit_suite/<int:s_id>')
def edit_suite(s_id=None):
    return f'get project {s_id}'


@web.route('/create_suite')
def create_suite():
    return f'create project'


@web.route('/delete_suite/<int:s_id>')
def delete_suite(s_id=None):
    return f'delete project {s_id}'