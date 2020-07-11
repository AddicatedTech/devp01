#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 19:37
# @Author  : Addicated
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm
from flask_sqlalchemy import SQLAlchemy
import time
db = SQLAlchemy()
# 还没有对app进行绑定，可以延时进行绑定，先进行实体类的编写

# 这里是将每个模型类都会创建的字段进行单独封装，然后之后通过继承提高代码复用
# 但是这个Base并不需要建表，使用__abstract__=True
# 加上之后就不会在进行创建表了
class Base(db.Model):
	__abstract__ = True
	created_at = db.Column(db.Integer,default=int(time.time()))
	# 数据生成时间，数据修改时间
	updated_at = db.Column(db.Integer,default=int(time.time())
	                       ,onupdate=int(time.time()))
	# status
	status = db.Column(db.SmallInteger,default=1)

class User(db.Model,Base):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(32),nullable=False,default='',unique=True)

