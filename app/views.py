#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 17:21
# @Author  : Addicated
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from app import app

@app.route("/")
def index():
	return  'hello'

# 蓝图
# 一个app可能会分为多个模块
# 后台系统，
# 前端系统
# api接口  /test_case 云测平台
# api 同样存在版本不同的问题
# application 会包含多个子系统
# 蓝图 blueprint() app 衍生出来的
# 相当于一个插座