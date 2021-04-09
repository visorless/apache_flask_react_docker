from flask import render_template
from . import bp


@bp.route('/data')
def data():
    return 'bow and arrows'


# @bp.route('/')
# def hello_whale():
#     return 'bow and arrows'
