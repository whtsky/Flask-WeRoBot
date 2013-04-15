.. Flask-WeRoBot documentation master file, created by
   sphinx-quickstart on Fri Apr  5 23:26:27 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
.. module:: flask.ext.werobot


Flask-WeRoBot
=========================================
Flask-WeRoBot 是一个帮助你将 WeRoBot 集成进 Flask 的插件。
你只要创建一个 :class:`WeRoBot` 类，就可以轻松的在你的 Flask 应用中集成 `WeRoBot <http://werobot.readthedocs.org/en/latest/>`_ 。

入门
------

最简单的 Hello World ::

    from flask import Flask
    from flask.ext.werobot import WeRoBot

    app = Flask(__name__)
    robot = WeRoBot(app)

    @robot.handler
    def echo(message):
        return 'Hello World'

你可以像使用 `WeRoBot <http://werobot.readthedocs.org/en/latest/>`_ 一样使用 Flask-WeRoBot 。

当然，你也可以在实例化 :class:`WeRoBot` 时不传入 Flask App ，而是之后通过 :meth:`WeRoBot.init_app` 来给 Flask App 添加 WeRoBot 支持 ::

    from flask import Flask
    from flask.ext.werobot import WeRoBot

    robot = WeRoBot()


    @robot.handler
    def echo(message):
        return 'Hello World'


    def create_app():
        app = Flask(__name__)
        robot.init_app(app)
        return app

配置
------

===============  ========================= =============
名称               描述                      默认值
===============  ========================= =============
WEROBOT_TOKEN     微信 Token 值              None
WEROBOT_ROLE      Flask-WeRoBot 监听的地址   /wechat
===============  ========================= =============

API
----

.. autoclass:: WeRoBot
  :members: init_app

ChangeLog
-----------

Version v0.1.0
```````````````
+ 框架可用。