

# 各种各样的配置，在项目规模小的时候可以单独使用一个py文件用来储存配置
# 项目规模大的时候，最好使用一个包，里面存放各种环境下的配置
# 当有共有配置比较多的时候，使用一个类，然后让其他类进行继承即可
# 配置项要大写 BEBUG
# 通过pycharm的flask配置启动的话不会走app.py ，需要单独配置
# 配置需要注意的点
# 1，大写  2，几种导入方式
class BaseConfig:
	PER_PAGE = 10  # 每页显示数据数
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/demo'

class DevelopConfig(BaseConfig):
	DEBUG = True


# 引用方法，1, 定义一个变量来进行导入使用
config = DevelopConfig()
# 引用方法  2，初始化的时候进行