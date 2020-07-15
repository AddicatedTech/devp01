#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 20:09
# @Author  : Addicated
# @Site    : 
# @File    : init_project_data.py
# @Software: PyCharm
from app.web.models import ProjectInfo, db
from run import app

def add_project(nums):
	with app.app_context() as ctx:
		for i in range(nums):
			project = ProjectInfo(project_name=F"project{i}", simple_desc=F"project{i},简介")
			db.session.add(project)
			# 此时如果直接进行db的操作的话不会成功，因为没有推入上下文
			# 使用with as 打开上下文环境，将其推入
		db.session.commit()

if __name__ == "__main__":
	add_project(10)

