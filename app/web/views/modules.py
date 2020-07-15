
from flask import render_template

from app.web import web


@web.route('/list_modules')
def list_modules():
    return 'projects'

@web.route('/create_module')
def create_module():
    return 'projects'