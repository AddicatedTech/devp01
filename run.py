
'''
web 服务器运行
选用 gunicorn uwsgi waitress
'''
from flask import url_for
from app import create_app
# 将app init下app导入进来
app = create_app()  # 通过初始化方法产生的app ，配置类属性生效
print(app.url_map)
# url_for()

if __name__ == '__main__':
	# print("测试输出配置项" + app.config['DEBUG'])
	app.run(debug=app.config['DEBUG'])
	
