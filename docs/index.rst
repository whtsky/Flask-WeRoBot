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

.. attention::
  你可以在实例化 :class:`WeRoBot` 时传入一个 ``token`` ，或者随时通过修改 ``WeRoBot.token`` 的值来改变 token 。
  Flask-WeRoBot 会优先使用手动指定的 Token ，若没有手动指定才会使用配置文件中的 `` WEROBOT_TOKEN ``

API
----

.. autoclass:: WeRoBot
  :members: init_app

ChangeLog
-----------

Version v0.1.2
```````````````
+ 修复对 WeRoBot 0.4.0 的兼容性问题。感谢 

Version v0.1.1
```````````````
+ 支持手动修改 Token
+ 支持在同一应用中绑定多个微信机器人

Version v0.1.0
```````````````
+ 框架可用。