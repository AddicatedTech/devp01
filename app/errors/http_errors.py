#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 8:48
# @Author  : Addicated
# @Site    : 
# @File    : http_errors.py
# @Software: PyCharm

# 写一个处理 ajax 异常的异常类
# 具体的写法是继承Httpexception
import json

from werkzeug.exceptions import HTTPException


class JsonHTTPException(HTTPException):

	# 需要重写一些父类的方法
	def get_description(self,environ=None):
		return self.description

	def get_body(self, environ=None):
		return json.dumps(
			{'code':self.code,
			 'name':self.name,
			 'msg':self.get_description(environ)
			 }
		)

	def get_headers(self, environ=None):
		return [('Content-Type','application/json')]

class JsonValidateError(JsonHTTPException):
	# 验证不通过的时候错误代码定义
	code = 400

class JsonDatabaseError(JsonHTTPException):
	# 验证不通过
	code = 500