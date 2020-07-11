'''

初始化app 核心对象

配置相关的一些插件


'''

from flask import Flask
from app.config import config, DevelopConfig
from app.main.models import db
from flask_migrate import Migrate
app = Flask(__name__)
migrate = Migrate()

# 初始化一些项目环境所用的配置
# config = DevelopConfig  # 通过导包来引入配置属性，但是当配置多起来的时候不便于管理


def create_app():  # create_app 返回的app没有传入到app.py中， 成为导致配置属性未生效的原因
	# 初始化 db
	app.config.from_object(config)  # 从一个对象里面导入
	# 配置文件的加载需要放在前面

	db.init_app(app)
	# 初始化配置文件
	# migrate init
	migrate.init_app(app,db)
	# 自定义的错误处理机制
	# 模板过滤器
	# ------7.11----------
	# 蓝图定义之后需要注册  蓝图只需要使用一次，则即用即导入，避免出现循环导入
	from app.main import main
	app.register_blueprint(main)

	return app