from flask import render_template

# 处理错误
def errors_config(app):
    @app.errorhandler(404)
    def error_404(e):
        return render_template('error/404.html')