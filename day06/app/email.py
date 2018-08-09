# 异步发送邮件
def async_send(app, msg):
    # 通过with 管理线程
    with app.app_context():
        mail.send(msg)


def async_send_mail_util(subject, recipients, emailTmp, **kwargs):
    # 获取当前app
    app = current_app._get_current_object()
    msg = Message(subject=subject,
                  recipients=recipients,
                  sender=app.config['MAIL_USERNAME'])

    # 使用模板发送
    msg.html = render_template(emailTmp + '.html', **kwargs)
    # 创建一条线程
    t = threading.Thread(target=async_send, args=(app, msg), name='邮箱线程')
    # 线程名
    # daemon 守护主线程
    # 默认False，主线程死了，子线程依然跑
    # 如果为True ,主线程死了，子线程也死

    print(threading.current_thread().name)
    print(threading.current_thread().daemon)
    # 开启
    t.start()
