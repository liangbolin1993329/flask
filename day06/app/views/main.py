from flask import Blueprint,render_template

# 创建视图对象
main = Blueprint('main',__name__)

@main.route('/index/')
def index():
    return render_template('common/base.html')