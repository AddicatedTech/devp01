#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 21:27
# @Author  : Addicated
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

# 这个文件夹用来存放一些前段页面上使用的过滤器，
# 对字段进行一些过滤操作显示
# 之后前往app下init模块去添加过滤器
from datetime import datetime

def str_time(ts):
	return datetime.fromtimestamp(ts)