
'''
web 服务器运行
选用 gunicorn uwsgi waitress
'''



from app import create_app
# 将app init下app导入进来
app = create_app()  # 通过初始化方法产生的app ，配置类属性生效


if __name__ == '__main__':
	app.run(debug=app.config['DEBUG'])
