from flask import Flask, url_for
from flask.ext.werobot import WeRoBot

app = Flask(__name__)
robot = WeRoBot()

app.debug = True
app.config.from_pyfile('app.cfg')


@robot.handler
def reply(message):
    return 'Hello!'


robot.init_app(app)

another_robot = WeRoBot(token='abcdefg', enable_session=True)


@another_robot.handler
def another_reply(message):
    return "Hey, that's another robot!"


another_robot.init_app(app, endpoint='werobot_2',
                       rule='/wechat/2')


@app.route('/')
def index():
    return 'First WeRoBot will handle WeChat requests at %s <br />' \
           'Second WeRoBot will handle at %s' % (
               url_for('werobot'), url_for('werobot_2')
           )


if __name__ == '__main__':
    app.run()
