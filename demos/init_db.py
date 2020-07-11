#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 20:59
# @Author  : Addicated
# @Site    : 
# @File    : init_db.py
# @Software: PyCharm

#  引入 app db
from app import app,db


with app.app_context() as ctx:
	db.create_all()