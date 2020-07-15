#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 22:35
# @Author  : Addicated
# @Site    : 
# @File    : validators.py
# @Software: PyCharm

# 自定义验证器类来满足逻辑复杂的验证方法，
# 复习一下写法
from wtforms import ValidationError


class Unique():
	# 验证某个模型的某个字段是否在db中存在，即是否唯一
	# 实例Unique(Project,project.project_name)
	def __init__(self, db_class, db_column, msg=None):  # msg错误信息
		self.db_class = db_class
		self.db_column = db_column
		# self.msg = "" if msg is  None else	msg
		if msg is None:
			self.msg = "数据已经存在"
		else:
			self.msg = msg

	def __call__(self, form, field):
		# p1 form 表单对象 p2 验证字段
		# call 方法是一个验证器类的灵魂，是有固定写法的
		# 设定一个验证规则，通过即返回，未通过就抛出异常
		# 查询 db_class下面有没有
		res = self.db_class.query.filter(self.db_column==field.data).first()
		if res:
			raise ValidationError(self.msg)
		return res