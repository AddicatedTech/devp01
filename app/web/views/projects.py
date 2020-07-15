from app.errors.DataBbaseException import DataBaseException, UpdateDataException
from app.errors.http_errors import JsonDatabaseError, JsonValidateError
from app.web import web
from flask import request, render_template, abort, redirect, jsonify
from app.web.models import ProjectInfo
from app.web.forms import ProjectAddForm


@web.route("/list_projects")
def list_projects():
	# 自己生成假数据
	page = request.args.get('page', 1)  # 取第一页
	paginate = ProjectInfo.paginate(page)  # 在model中定义了有关分页的方法
	projects = paginate.items

	return render_template('projects.html', projects=projects,
	                       paginate=paginate)


# 逆向开发思路，首先去看目标页面中需要的东西 projects ,分页器


# TODO 分页
# 展示的不完全数据
# 注册过滤器，分离
# ----------------7.14
# 做验证的时候要在蓝图路径下新建一个表单验证层来存放表单类和验证方法代码
# 分页，在实体类定义的时候将分页方法定义到实体类中，通过模板渲染渲染到前端页面
# 查询方法同分页一样，注意这样的方式定义成类方法，因为需要满足直接通过模型类去调用
# 写业务逻辑，先在视图层理清楚思路，然后一级一级的向底层去实现，由终至始
@web.route("/create_project")
def create_project():
	#  首先需要考虑的是get请求  展示输入框，
	if request.method == "GET":
		form = ProjectAddForm()  # 定义一个form表单 然后渲染到前端页面的时候传进去
		return render_template('project.html', form=form)

	# 之后post请求  提交数据请求
	# 1 接收前端传回来的表单内容
	# 2 校验 project_name 项目名称唯一 simple_desc

	form = ProjectAddForm(request.form)  # 完成form表单的初始化
	if form.validate():

		try:
			ProjectInfo.insert(form.data)
			return redirect('/list_projects')
		except DataBaseException as e:
			# 比较友好的方法是出现异常之后重定向，将错误信息回显前端
			msg = "请求数据不合理"
			return render_template('project.html', form=form,
			                       error_msg=msg)

	# 这里抛出异常为了返回给前端告知操作没有成功

	return render_template('project.html', form=form)


# 保存，数据层，project.add_by_form(form)
# 重定向到 项目列表
# 3 如果校验不通过，重定向到页面，显示错误信息
# 4 校验通过，插入数据库，重定向到 projects.html


# 分层情况  1，验证层 projectAddForm() 2,验证器层 Unique()
# 3, 数据处理层 model project.insert()  4,错误处理层 exception


# 编辑项目
# 不紧要展示 get post
# 数据校验
@web.route('/edit_project/<int:p_id>')
def edit_project(p_id):
	# get 请求则需要跳转到编辑项目的页面并且将数据渲染至页面
	project = ProjectInfo.query.get(p_id)
	if not project:
		# 没有该项目的话直接重定向到项目列表页面
		return redirect('/list_projects')
	if request.method == "GET":
		form = ProjectAddForm()
		return render_template('project_edit.html',
		                       form=form, project=project)
	form = ProjectAddForm(request.form)
	if form.validate():
		try:
			ProjectInfo.update(form.data)
			return redirect('/list_projects')
		except UpdateDataException as e:
			msg = "更新数据到DB失败"
			return render_template('project.html', form=form, error_msg=msg)

	return render_template('project.html', form=form)


@web.route('/delete_project', methods=['GET', 'POST'])
def delete_project():
	# 获取请求数据
	p_id = request.json.get("id")
	try:
		res = ProjectInfo.query.get(int(p_id))
		if res:
			# 找到即删除 res即为projectinfo对象
			res.delete()
		# 因为发送的是一个ajax请求，所以返回的会是一个json数据
		raise JsonDatabaseError('没有这个项目')
		# return jsonify({'msg': '没有这个项目'})
	except Exception as e:
		raise JsonValidateError("id格式不正确")
		# return jsonify({'msg': 'id 格式不正确'})

# 验证p_id所对应的数据在db中是否存在


# 删除项目
# 逻辑删除
