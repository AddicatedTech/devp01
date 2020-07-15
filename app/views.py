# from app import app
#
# @app.route("/")
# def index():
# 	return  'hello'

# 蓝图
# 一个app可能会分为多个模块
# 后台系统，
# 前端系统
# api接口  /test_case 云测平台
# api 同样存在版本不同的问题
# application 会包含多个子系统
# 蓝图 blueprint() app 衍生出来的
# 相当于一个插座
# -------------------------7.11
# 通过各种各样的蓝图将子系统配到application中
# 可以共享一些app的设置，但是各个蓝图又有各自的执行逻辑
# 蓝图的使用
# 定义一个蓝图
# from flask import Blueprint
# web = Blueprint("web",__name__)  # 第一个参数为蓝图的名字
# 定义之后想要使用需要在 核心对象初始化的时候进行注册
# app.register_blueprint() 参数即是 蓝图对象名
# 给蓝图进行路由注册的时候不再使用@app.route() 而是使用 @蓝图名.route()

# 蓝图注册
# from flask import Blueprint
# web = Blueprint("web",__name__,url_prefix=)
# 第一个 参数为蓝图的名字,
# 第二个 参数为固定__name__,
# 第三个 url_prefix urlpattern的前缀

# 1 定义的时候需要起名字
# 2 路由要导入到定义蓝图的py文件下
# 3，初始化的时候 app.register_blueprint(蓝图名)

# 前端ui框架的选择
# amaze-ui
# semantic-UI
# bootstrap
# ------------------7.12
# 蓝图的功能