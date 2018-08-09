from flask import Flask
from app.config import config
from app.extensions import extension_config
from app.views import blueprint_config
from app.errors import errors_config


# 封装创建方法
# 传入环境名
def create_app(config_name):
    # 创建app应用
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(config.get(config_name))
    # 额外初始化
    config.get(config_name).init_app(app)

    # 加载扩展
    extension_config(app)

    # 注册蓝本
    blueprint_config(app)

    # 错误捕捉
    errors_config(app)

    return app