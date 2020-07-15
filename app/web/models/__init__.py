from flask_sqlalchemy import SQLAlchemy, BaseQuery
from flask import current_app
import time
# 还没有对app进行绑定，可以延时进行绑定，先进行实体类的编写

# 这里是将每个模型类都会创建的字段进行单独封装，然后之后通过继承提高代码复用
# 但是这个Base并不需要建表，使用__abstract__=True
# 加上之后就不会在进行创建表了
from sqlalchemy import desc

from app.errors.DataBbaseException import DataBaseException, UpdateDataException, DeleteDataException

class MyBaseQuery(BaseQuery):
	def filter_by(self, **kwargs):
		kwargs.setdefault('status',1)
		# 设置默认值，会去查找status有没有值，没有默认设置成1
		return super(MyBaseQuery, self).filter_by(**kwargs)



db = SQLAlchemy(query_class=MyBaseQuery)  # 定义之后仍然需要在db对象初始化的时候进行指定


class Base(db.Model):
	__abstract__ = True
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.Integer, default=int(time.time()))
	# 数据生成时间，数据修改时间
	updated_at = db.Column(db.Integer, default=int(time.time())
	                       , onupdate=int(time.time()))
	# status
	status = db.Column(db.SmallInteger, default=1)

	# 思考都有哪些共有的方法需要写在base下被各个实体类继承
	# 查询所有属性
	# 分页
	@classmethod
	def all(cls):
		return cls.query.filter_by().order_by(desc(cls.updated_at)).all()

	@classmethod
	def paginate(cls, page):
		# 在这里没有进行过滤，所以进行了逻辑删除之后的项目依然会显示在页面上
		#  所以先做一个过滤，滤掉已经删除了的项目 但是很多地方都需要进行查询，
		# 如果都写query.filter_by的话工作量巨大且不效率不现实
		# 可以重写query方法  这个涉及到orm框架的二次开发
		return cls.query.filter_by().paginate(
			page=int(page), per_page=current_app.config['PER_PAGE'],
			error_out=False
		)


class User(Base):
	username = db.Column(db.String(32), nullable=False, default='', unique=True)


class ProjectInfo(Base):
	project_name = db.Column(db.String(32), nullable=False, default='', unique=True)
	simple_desc = db.Column(db.String(50), nullable=False, default='', unique=True)
	# 在这里设置一个关系声明，关联到moudles
	modules = db.relationship("ModuleInfo",backref= 'project',lazy='dynamic')
	# dynamic 返回一个query对象，还需要调用filter_by().all()方法
	# select 直接返回查询到的数据
	# 删除状态
	DELETE_STATUS = 0

	@classmethod
	def insert(cls, data):
		# 添加新的项目
		# data {"project_name":}
		project = ProjectInfo(
			project_aname=data.get("project_name", ''),  # 获取到 project_name 没获取到就按照后面空值
			simple_desc=data.get("simple_desc", '')
		)
		try:
			db.session.add(project)
			db.session.commit()
		except Exception as e:
			# logger记录
			# current_app.logger.error('project 保存出错')
			# 抛出异常  如果需要自己控制异常的话，需要在app下创建一个进行自定义异常控制
			raise DataBaseException("project数据异常")

	#   这里抛出异常是让后端去进行处理
	# return null
	# db.session.rollback()

	def update(self, data):
		# 更新项目信息  因为调用处上下文中已经获得了project独享
		# 便不需要再写成类方法
		self.project_aname = data.get("project_name", ''),  # 获取到 project_name 没获取到就按照后面空值
		self.simple_desc = data.get("simple_desc", '')
		try:
			db.session.add(self)
			db.session.commit()
			return self
		except Exception as e:
			# logger记录
			current_app.logger.error('project 更新出错')
			# 抛出异常  如果需要自己控制异常的话，需要在app下创建一个进行自定义异常控制
			raise UpdateDataException("project更新异常")

	#   这里抛出异常是让后端去进行处理
	# return null
	# db.session.rollback()

	def delete(self):
		# 删除记录 逻辑删除
		# bug会存在什么问题
		# 删除了之后项目还会展示出来
		# 删除完了之后 module，case 还能用嘛？ 级联删除
		self.status = self.DELETE_STATUS

		try:
			db.session.add(self)
			db.session.commit()
			return self
		except Exception as e:
			# logger记录
			current_app.logger.error('project 删除出错')
			# 抛出异常  如果需要自己控制异常的话，需要在app下创建一个进行自定义异常控制
			raise DeleteDataException("project删除发生异常")
# 二次开发的思路
# 在学完用法之后，还需要去看原码，不看原码的话，只能被框架支配，
# 不能实现定制个性化功能，代码冗余

# 接口和项目是多对一关系
class ModuleInfo(Base):
	module_name = db.Column(db.String(20),nullable=False)
	simple_desc = db.Column(db.String(20),default='')
	project_id = db.Column(db.INT,db.ForeignKey("project_info.id"))

	@property
	def case_records(self):
		# 获取module 可用的测试用例
		return self.test_case.filter_by().all()


# 测试用例和接口也是多对一的关系
class CaseInfo(Base):
	# 测试用例表
	type = db.Column(db.SmallInteger,default=1)
	name = db.Column(db.String(20),nullable=False)
	include = db.Column(db.String(512))
	request = db.Column(db.Text)
	module_id = db.Column(db.INT,db.ForeignKey('module_info.id'))

# 全局csrf 校验
# 在初始化的时候设置一 csrfprotect()
# 在ajax中使用全局csrftoken验证的时候需要


# 接口自动化测试的框架
# httprunner依赖
# 执行解析动作是使用yaml格式的用例
# httprunner 详细了解






