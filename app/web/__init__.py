#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 19:06
# @Author  : Addicated
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

# 进行初始化蓝图
from flask import Blueprint

web = Blueprint("web", __name__)

# 视图路由 需要导入，，不然访问不到
from .views import index, cases, modules, projects,suites
# 需要挂在到各个不同的视图函数，即路由project
# 蓝图可以共享app的静态资源与模板
