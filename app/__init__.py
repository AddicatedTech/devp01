'''

初始化app 核心对象

配置相关的一些插件


'''

from flask import Flask
from app.config import config, DevelopConfig

app = Flask(__name__)


# 初始化一些项目环境所用的配置
# config = DevelopConfig  # 通过导包来引入配置属性，但是当配置多起来的时候不便于管理


def create_app():  # create_app 返回的app没有传入到app.py中， 成为导致配置属性未生效的原因
	'''初始化'''
	# 初始化 db
	# 初始化配置文件
	app.config.from_object(config)  # 从一个对象里面导入
	# 自定义的错误处理机制
	# 模板过滤器

	return app
