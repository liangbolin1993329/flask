from flask_script import Manager
from app import create_app
import os

config_name = os.environ.get('CONFIG_NAME') or 'default'

app = create_app(config_name)

manager = Manager(app)

@app.route('/')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    manager.run()
