#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 19:16
# @Author  : Addicated
# @Site    :
# @File    : index.py
# @Software: PyCharm
from flask import render_template

from app.web import web
from app.web.models import ProjectInfo


@web.route('/')
def index():
	projects = ProjectInfo.query.all()
	return render_template("index.html",
	                       projects=projects)
