from flask import Flask, url_for
from flask.ext.werobot import WeRoBot

WeRoBot_Token = 'tokenhere'

app = Flask(__name__)
robot = WeRoBot()

app.debug = True
app.config.from_object(__name__)


@robot.handler
def reply():
    return 'Hello!'

robot.init_app(app)

@app.route('/')
def index():
    return 'WeRoBot will handle WeChat requests at %s' % url_for('werobot')

if __name__ == '__main__':
    app.run()