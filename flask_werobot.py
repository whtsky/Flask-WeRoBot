"""
    Flask-WeRoBot
    ---------------

    Adding WeRoBot support to Flask.

    :copyright: (c) 2013 by whtsky.
    :license: BSD, see LICENSE for more details.
"""

__version__ = '0.1.0'


import werobot
from flask import Flask


class WeRoBot(werobot.WeRoBot):
    def __init__(self, rule, app=None):
        super(WeRoBot, self).__init__(token='temptoken')
        self.rule = rule
        if app is not None:
            self.init_app(app)
        else:
            self._app = None

    def init_app(self, app):
        assert isinstance(app, Flask)
        self._app = app
        token = app.config.get('werobot_token')

        from werobot.utils import check_token, check_signature
        from werobot.parser import parse_user_msg
        from werobot.reply import create_reply

        if not check_token(token):
            raise AttributeError('%s is not a vaild token.' % token)
        self.token = token

        from flask import request, make_response, abort

        def handler():
            if not check_signature(token,
                                   request.args.get('timestamp', ''),
                                   request.args.get('nonce', ''),
                                   request.args.get('signature', '')):
                return 'Unvailed request.'
            if request.method == 'GET':
                return request.args['echostr']

            body = request.data
            message = parse_user_msg(body)
            reply = self._get_reply(message)
            if not reply:
                return ''
            response = make_response(create_reply(reply, message=message))
            response.headers['content_type'] = 'application/xml'
            return response

        app.add_url_rule(self.rule, endpoint='werobot',
                         view_func=handler, methods=['GET', 'POST'])
