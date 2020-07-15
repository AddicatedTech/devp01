# 初始化核心对象，进行一些项目中的配置
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from app.config import config, DevelopConfig
from flask_migrate import Migrate
from app.web.models import db

# 初始化一些项目环境所用的配置
# config = DevelopConfig  # 通过导包来引入配置属性，但是当配置多起来的时候不便于管理
from app.web.templates_env import str_time

csrf = CSRFProtect()


def create_app():  # create_app 返回的app没有传入到app.py中， 成为导致配置属性未生效的原因
	app = Flask(__name__)
	app.config.from_object(config)  # 从一个对象里面导入
	# 初始化 db
	# 配置文件的加载需要放在前面
	db.init_app(app)
	# 初始化配置文件
	# migrate init
	migrate = Migrate(app, db)
	# migrate.init_app(app, db)

	# 自定义的错误处理机制
	# 模板过滤器
	# ------7.11----------
	# 蓝图定义之后需要注册  蓝图只需要使用一次，则即用即导入，避免出现循环导入
	from app.web import web
	app.register_blueprint(web)
	# -------7.13
	# 添加过滤器
	app.add_template_filter(str_time)

	# csrf  flask 的任何插件在使用的时候都要与app进行绑定
	# 代码的话就是任何插件都会有init_app方法来进行绑定初始化
	csrf.init_app(app)
	return app
# --------------------- 7.12
