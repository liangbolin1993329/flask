from .main import main

# 蓝本元组 二维(蓝本，‘路由’)
DEFAULT_BLUEPRINT = (
    (main,''),
)
# 注册
def blueprint_config(app):
    for blueprint,prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint,url_prefix=prefix)