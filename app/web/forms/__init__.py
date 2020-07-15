#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 22:15
# @Author  : Addicated
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,IntegerField
from wtforms.validators import DataRequired, Length


# project name 的字段是unique唯一的，所以应该单独写一个验证方法
# 自定义验证器
# 新建一个类 思考一下，这个自定义的验证类是会被多次复用的，所以要定义成具有通用性的
# 思考变的部分都有哪一些，，project
from app.web.forms.validators import Unique
from app.web.models import ProjectInfo


class ProjectAddForm(FlaskForm):
	form_model = ProjectInfo  # 思路，用一个变量名去接受实体类，然后之后只修改变量即可，便于维护
	project_name = StringField(label='项目名称',
	                           validators=[DataRequired(), Length(max=64, min=1)
	                                       ,Unique(form_model,form_model.project_name)])


	simple_desc = TextAreaField(label='项目描述', validators=[Length(max=512, min=0)])

class ProjectDeleteForm(FlaskForm):
	id = IntegerField()