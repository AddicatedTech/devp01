#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 19:16
# @Author  : Addicated
# @Site    : 
# @File    : index.py
# @Software: PyCharm
from app.main import main


@main.route('/')
def index():
	return 'here is a blueprint'